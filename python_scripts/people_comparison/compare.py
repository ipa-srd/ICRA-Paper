import matplotlib.pyplot as plt
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

f, axarr = plt.subplots(3,2,figsize=(15,10))

axarr[0,0].plot(data[:,1], false_neg_1, label="my leg detector")
axarr[0,0].plot(data[:,1], false_neg_2, label="ros leg_detector (50% threshold)")
axarr[0,0].plot(data[:,1], false_neg_3, label="ros leg_detector (70% threshold)")
axarr[0,0].plot(data[:,1], false_neg_4, label="ros leg_detector (30% threshold)")

axarr[0,0].set_xlabel("Number of people to label")
axarr[0,0].set_ylabel("False negative rate")

axarr[0,0].grid()
axarr[0,0].margins(0.05, 0.1)

# ----------------------------------------
axarr[1,0].plot(data[:,1], false_pos_1, label="my leg detector")
axarr[1,0].plot(data[:,1], false_pos_2, label="ros leg_detector (50% threshold)")
axarr[1,0].plot(data[:,1], false_pos_3, label="ros leg_detector (70% threshold)")
axarr[1,0].plot(data[:,1], false_pos_4, label="ros leg_detector (30% threshold)")

axarr[1,0].set_xlabel("Number of people to label")
axarr[1,0].set_ylabel("False positive rate")

axarr[1,0].grid()
axarr[1,0].margins(0.05, 0.1)

# ----------------------------------------
axarr[0,1].plot(data[:,1], F_1, label="my leg detector")
axarr[0,1].plot(data[:,1], F_2, label="ros leg_detector (50% threshold)")
axarr[0,1].plot(data[:,1], F_3, label="ros leg_detector (70% threshold)")
axarr[0,1].plot(data[:,1], F_4, label="ros leg_detector (30% threshold)")

axarr[0,1].set_xlabel("Number of people to label")
axarr[0,1].set_ylabel("F-Measure")

axarr[0,1].grid()
axarr[0,1].margins(0.05, 0.1)

# ----------------------------------------
axarr[1,1].plot(data[:,1], prec_1, label="my leg detector")
axarr[1,1].plot(data[:,1], prec_2, label="ros leg_detector (50% threshold)")
axarr[1,1].plot(data[:,1], prec_3, label="ros leg_detector (70% threshold)")
axarr[1,1].plot(data[:,1], prec_4, label="ros leg_detector (30% threshold)")

axarr[1,1].set_xlabel("Number of people to label")
axarr[1,1].set_ylabel("Precission")

axarr[1,1].grid()
axarr[1,1].margins(0.05, 0.1)

# ----------------------------------------
axarr[2,0].plot(data[:,1], rec_1, label="my leg detector")
axarr[2,0].plot(data[:,1], rec_2, label="ros leg_detector (50% threshold)")
axarr[2,0].plot(data[:,1], rec_3, label="ros leg_detector (70% threshold)")
axarr[2,0].plot(data[:,1], rec_4, label="ros leg_detector (30% threshold)")

axarr[2,0].set_xlabel("Number of people to label")
axarr[2,0].set_ylabel("Recall")

axarr[2,0].grid()
axarr[2,0].margins(0.05, 0.1)

# ----------------------------------------
axarr[2,1].plot(-1,-1, label="my leg detector")
axarr[2,1].plot(-1,-1, label="ros leg_detector (50% threshold)")
axarr[2,1].plot(-1,-1, label="ros leg_detector (70% threshold)")
axarr[2,1].plot(-1,-1, label="ros leg_detector (30% threshold)")
axarr[2,1].set_xlim(0,1)
axarr[2,1].legend()

plt.show()
