import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
import numpy as np

data = np.genfromtxt("data.csv", delimiter="\t")

def get_F(TP, FP, FN):
    prec = TP/(TP+FP)
    rec = TP/(TP+FN)
    F = 2*prec*rec/(prec+rec)
    return F, prec, rec

false_neg_1 = data[:,3]/data[:,1]
false_neg_2 = data[:,7]/data[:,1]
false_neg_3 = data[:,11]/data[:,1]
false_neg_4 = data[:,15]/data[:,1]

false_pos_1 = (data[:,5])/data[:,1]
false_pos_2 = (data[:,9])/data[:,1]
false_pos_3 = (data[:,13])/data[:,1]
false_pos_4 = (data[:,17])/data[:,1]

true_pos_1 = (data[:,2])/data[:,1]
true_pos_2 = (data[:,6])/data[:,1]
true_pos_3 = (data[:,10])/data[:,1]
true_pos_4 = (data[:,14])/data[:,1]

F_1, prec_1, rec_1 = get_F(true_pos_1, false_pos_1, false_neg_1)
F_2, prec_2, rec_2 = get_F(true_pos_2, false_pos_2, false_neg_2)
F_3, prec_3, rec_3 = get_F(true_pos_3, false_pos_3, false_neg_3)
F_4, prec_4, rec_4 = get_F(true_pos_4, false_pos_4, false_neg_4)

f, axarr = plt.subplots(3,1,figsize=(3.6,5.5), sharex=True)

# gs1 = gridspec.GridSpec(3, 1)
# gs1.update(wspace=0.025, hspace=0.0) # set the spacing between axes. 

# axarr[0] = plt.subplot(gs1[0])

# axarr[0,0].plot(data[:,1], false_neg_1, label="my leg detector")
# axarr[0,0].plot(data[:,1], false_neg_2, label="ros leg_detector (50% threshold)")
# axarr[0,0].plot(data[:,1], false_neg_3, label="ros leg_detector (70% threshold)")
# axarr[0,0].plot(data[:,1], false_neg_4, label="ros leg_detector (30% threshold)")

# axarr[0,0].set_xlabel("Number of people to label")
# axarr[0,0].set_ylabel("False negative rate")

# axarr[0,0].grid()
# axarr[0,0].margins(0.05, 0.1)

# ----------------------------------------
# axarr[1,0].plot(data[:,1], false_pos_1, label="my leg detector")
# axarr[1,0].plot(data[:,1], false_pos_2, label="ros leg_detector (50% threshold)")
# axarr[1,0].plot(data[:,1], false_pos_3, label="ros leg_detector (70% threshold)")
# axarr[1,0].plot(data[:,1], false_pos_4, label="ros leg_detector (30% threshold)")

# axarr[1,0].set_xlabel("Number of people to label")
# axarr[1,0].set_ylabel("False positive rate")

# axarr[1,0].grid()
# axarr[1,0].margins(0.05, 0.1)

# ----------------------------------------
axarr[0].plot(data[:,1], F_1, "-", label="my leg detector")
axarr[0].plot(data[:,1], F_2, "--", label="ros leg_detector (50% threshold)")
axarr[0].plot(data[:,1], F_3, "-.", label="ros leg_detector (70% threshold)")
axarr[0].plot(data[:,1], F_4, "-", dashes=(5,5), label="ros leg_detector (30% threshold)")

# axarr[0,0].set_xlabel("Number of people to label")
axarr[0].set_ylabel(r"F-Measure")

axarr[0].grid()
axarr[0].margins(0.05, 0.1)
axarr[0].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# ----------------------------------------
axarr[1].plot(data[:,1], prec_1, "-", label="my leg detector")
axarr[1].plot(data[:,1], prec_2, "--", label="ros leg_detector (50% threshold)")
axarr[1].plot(data[:,1], prec_3, "-.", label="ros leg_detector (70% threshold)")
axarr[1].plot(data[:,1], prec_4, "-", dashes=(5,5), label="ros leg_detector (30% threshold)")

# axarr[1,1].set_xlabel("Number of people to label")
axarr[1].set_ylabel(r"Precission")

axarr[1].grid()
axarr[1].margins(0.05, 0.1)

# ----------------------------------------
axarr[2].plot(data[:,1], rec_1, "-", label="Convoluted leg detector")
axarr[2].plot(data[:,1], rec_2, "--", label="Adaboost leg detector (50% threshold)")
axarr[2].plot(data[:,1], rec_3, "-.", label="Adaboost leg detector (70% threshold)")
axarr[2].plot(data[:,1], rec_4, "-", dashes=(5,5), label="Adaboost leg detector (30% threshold)")

# axarr[2,0].set_xlabel("Number of people to label")
axarr[2].set_ylabel(r"Recall")

axarr[2].grid()
axarr[2].margins(0.05, 0.1)
axarr[2].set_xlabel(r"Number of people")
axarr[2].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# ----------------------------------------
# axarr[2,1].plot(-1,-1, label="my leg detector")
# axarr[2,1].plot(-1,-1, label="ros leg_detector (50% threshold)")
# axarr[2,1].plot(-1,-1, label="ros leg_detector (70% threshold)")
# axarr[2,1].plot(-1,-1, label="ros leg_detector (30% threshold)")
# axarr[2,1].set_xlim(0,1)
# axarr[2,1].legend()


ax2 = axarr[0].twiny()
x2_ticks = list(data[:,1][:7])
x2_ticks.append(data[:,1][-1])
x2 = list(data[:,0][:7])
x2.append(data[:,0][-1])
ax2.set_xlim(axarr[0].get_xlim())
ax2.set_xticks(x2_ticks)
ax2.set_xticklabels([d for d in x2])
ax2.set_xlabel(r"Radius around robot [$m$]")
# ax2.set_xlabel(l2)
# axarr[1].legend()
axarr[2].legend(loc=9, bbox_to_anchor=(0.5, -0.4))
plt.tight_layout()

plt.savefig("people_det.pdf", bbox_inches="tight")
plt.savefig("people_det.pgf", bbox_inches="tight")
# plt.show()
