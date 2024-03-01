import matplotlib.pyplot as plt
import numpy as np


sizes_1 = np.array([10, 15, 25, 35, 45, 55])
times_1 = np.array([31, 38, 104, 324, 869, 2063])

sizes_3 = np.array([55, 65, 75, 85, 95, 105, 115, 125])
times_3 = np.array([2200, 3230, 4556, 6394, 8465, 11312, 14551, 18551])

sizes_4 = np.array([75, 85, 95, 105, 115, 125, 135, 145])
times_4 = np.array([4184, 5630, 7351, 9473, 11774, 14876, 18146, 22070])

sizes_5 = np.array([95, 105, 115, 125, 135, 145, 155])
times_5 = np.array([6708, 8434, 10337, 12896, 15618, 18959, 22831])

sizes_6 = np.array([95, 105, 115, 125, 135, 145, 155])
times_6 = np.array([6627, 8456, 10179, 12141, 14564, 17349, 20756])

sizes_7 = np.array([135, 145, 155, 165])
times_7 = np.array([13724, 16332, 19358, 22189])

sizes_1 = sizes_1**2 * 2
sizes_3 = sizes_3**2 * 2
sizes_4 = sizes_4**2 * 2
sizes_5 = sizes_5**2 * 2
sizes_6 = sizes_6**2 * 2
sizes_7 = sizes_7**2 * 2


fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(sizes_1, times_1, marker="d", label="1x1")
ax.plot(sizes_3, times_3, marker="d", label="3x3")
ax.plot(sizes_4, times_4, marker="d", label="4x4")
ax.plot(sizes_5, times_5, marker="d", label="5x5")
ax.plot(sizes_6, times_6, marker="d", label="6x6")
ax.plot(sizes_7, times_7, marker="d", label="7x7")

ax.plot(
    [sizes_3[0] - 500, sizes_7[1]],
    [times_3[0] - 400, times_7[1] - 400],
    ls="--",
    color="r",
    linewidth=3,
)

ax.set_xlim([0, None])
ax.set_ylim([0, None])
ax.set_xlabel("Number of atoms", fontsize=25)
ax.set_ylabel("Hessian inference time (s)", fontsize=25)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.legend(title="Patches grid", title_fontsize=20, fontsize=20)

plt.tight_layout()

# plt.show()
plt.savefig("timing_vs_grids_with_fit.pdf")
