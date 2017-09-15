import matplotlib.pyplot as plt
import numpy as np

# radius, number of points, correct points, false positives, false negatives
data = np.array(
        [[1.0, 146, 1.0, 0.0, 0.0],
        [1.4, 569, 1.0, 0.0, 0.0],
        [1.8, 1877, 0.992072, 0.0, 0.006102],
        [2.2, 3255, 0.968174, 0.0, 0.024736],
        [2.6, 4725, 0.945567, 0.0, 0.042315],
        [3.0, 5537, 0.900033, 0.024444, 0.080153],
        [3.4, 6036, 0.851460, 0.082817, 0.124590],
        [3.8, 6372, 0.819550, 0.083674, 0.153568],
        [4.2, 6539, 0.784053, 0.081821, 0.187268],
        [4.6, 6600, 0.749404, 0.081114, 0.218689],
        [5.0, 6603, 0.704922, 0.081089, 0.292180]])

fig = plt.figure(figsize=(3.6,2.0))
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

x1 = data[:,1]
x2_ticks = list(x1[:7])
x2_ticks.append(x1[-1])
x2 = list(data[:,0][:7])
x2.append(data[:,0][-1])
l1 = r"Number of points to label"
l2 = r"Radius around robot [$m$]"

ax1.plot(x1, data[:,2], label="correct", color="b")
# ax1.plot(x1, data[:,3], label="fp", color="orange")
# ax1.plot(x1, data[:,4], label="fn", color="g")
# ax1.plot(x1, data[:,2], "x", label=None)
# ax1.plot(x1, data[:,3], "x", label=None)
# ax1.plot(x1, data[:,4], "x", label=None)
ax1.set_xlabel(l1)

ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(x2_ticks)
ax2.set_xticklabels([d for d in x2])
ax2.set_xlabel(l2)
ax2.set_ylabel("Accuracy")

# ax1.legend()
plt.tight_layout()
# plt.show()

plt.savefig('radius_detection.pdf')
plt.savefig('radius_detection.pgf')
