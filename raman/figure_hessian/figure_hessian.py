import pickle
import numpy as np
import matplotlib.pyplot as plt

combinations = [
    (2, 6, 128),
    (3, 5, 128),
    (3, 6, 128),
    (3, 6, 256),
    (3, 6, 64),
    (3, 7, 128),
    (4, 6, 128),
    (6, 6, 128),
]

data = {}
for comb in combinations:
    with open(f"results_hessian_{comb[0]}_{comb[1]}_{comb[2]}.pkl", "rb") as f:
        data[f"{comb[0]}_{comb[1]}_{comb[2]}"] = pickle.load(f)[
            f"{comb[0]}_{comb[1]}_{comb[2]}"
        ]

fig, ax = plt.subplots(ncols=3, nrows=2, figsize=(16, 10))

(ax1, ax2, ax3), (ax4, ax5, ax6) = ax

ax1.set_title("Interaction Blocks", fontsize=17)
ax1.set_ylabel("Memory (MB) per atom", fontsize=17)
ax1.set_xlabel("Number of atoms", fontsize=17)
ax1.plot(
    data["2_6_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["2_6_128"]["mems"] / data["2_6_128"]["sizes"] ** 2 * 2),
    label=f"2",
)
ax1.plot(
    data["3_6_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_6_128"]["mems"] / data["3_6_128"]["sizes"] ** 2 * 2),
    label=f"3",
)
ax1.plot(
    data["4_6_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["4_6_128"]["mems"] / data["4_6_128"]["sizes"] ** 2 * 2),
    label=f"4",
)
ax1.plot(
    data["6_6_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["6_6_128"]["mems"] / data["6_6_128"]["sizes"] ** 2 * 2),
    label=f"6",
)
ax1.legend(fontsize=12)

ax4.set_ylabel("Inference time (s) per atom", fontsize=17)
ax4.set_xlabel("Number of atoms", fontsize=17)
ax4.plot(
    data["2_6_128"]["sizes"] ** 2 * 2,
    data["2_6_128"]["times"] / data["2_6_128"]["sizes"] ** 2 * 2,
    label="2",
)
ax4.plot(
    data["3_6_128"]["sizes"] ** 2 * 2,
    data["3_6_128"]["times"] / data["3_6_128"]["sizes"] ** 2 * 2,
    label="3",
)
ax4.plot(
    data["4_6_128"]["sizes"] ** 2 * 2,
    data["4_6_128"]["times"] / data["4_6_128"]["sizes"] ** 2 * 2,
    label="4",
)
ax4.plot(
    data["6_6_128"]["sizes"] ** 2 * 2,
    data["6_6_128"]["times"] / data["6_6_128"]["sizes"] ** 2 * 2,
    label="6",
)
ax4.legend(fontsize=12)

ax2.set_title("Cutoff", fontsize=17)
ax2.set_ylabel("Memory (Mb) per atom", fontsize=17)
ax2.set_xlabel("Number of atoms", fontsize=17)
ax2.plot(
    data["3_5_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_5_128"]["mems"] / data["3_5_128"]["sizes"] ** 2 * 2),
    label="5 A",
)
ax2.plot(
    data["3_6_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_6_128"]["mems"] / data["3_6_128"]["sizes"] ** 2 * 2),
    label="6 A",
)
ax2.plot(
    data["3_7_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_7_128"]["mems"] / data["3_7_128"]["sizes"] ** 2 * 2),
    label="7 A",
)
ax2.legend(fontsize=12)

ax5.set_ylabel("Inference time (s) per atom", fontsize=17)
ax5.set_xlabel("Number of atoms", fontsize=17)
ax5.plot(
    data["3_5_128"]["sizes"] ** 2 * 2,
    data["3_5_128"]["times"] / data["3_5_128"]["sizes"] ** 2 * 2,
    label="5 A",
)
ax5.plot(
    data["3_6_128"]["sizes"] ** 2 * 2,
    data["3_6_128"]["times"] / data["3_6_128"]["sizes"] ** 2 * 2,
    label="6 A",
)
ax5.plot(
    data["3_7_128"]["sizes"] ** 2 * 2,
    data["3_7_128"]["times"] / data["3_7_128"]["sizes"] ** 2 * 2,
    label="7 A",
)
ax5.legend(fontsize=12)

ax3.set_title("Embedding size", fontsize=17)
ax3.set_ylabel("Memory (Mb) per atom", fontsize=17)
ax3.set_xlabel("Number of atoms", fontsize=17)
ax3.plot(
    data["3_6_64"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_6_64"]["mems"] / data["3_6_64"]["sizes"] ** 2 * 2),
    label="64",
)
ax3.plot(
    data["3_6_128"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_6_128"]["mems"] / data["3_6_128"]["sizes"] ** 2 * 2),
    label="128",
)
ax3.plot(
    data["3_6_256"]["sizes"] ** 2 * 2,
    (1 / 8) * (data["3_6_256"]["mems"] / data["3_6_256"]["sizes"] ** 2 * 2),
    label="256",
)
ax3.legend(fontsize=12)

ax6.set_ylabel("Inference time (s) per atom", fontsize=17)
ax6.set_xlabel("Number of atoms", fontsize=17)
ax6.plot(
    data["3_6_64"]["sizes"] ** 2 * 2,
    data["3_6_64"]["times"] / data["3_6_64"]["sizes"] ** 2 * 2,
    label="64",
)
ax6.plot(
    data["3_6_128"]["sizes"] ** 2 * 2,
    data["3_6_128"]["times"] / data["3_6_128"]["sizes"] ** 2 * 2,
    label="128",
)
ax6.plot(
    data["3_6_256"]["sizes"] ** 2 * 2,
    data["3_6_256"]["times"] / data["3_6_256"]["sizes"] ** 2 * 2,
    label="256",
)
ax6.legend(fontsize=12)

for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.set_xlim([0, None])
    ax.grid("on")
    ax.xaxis.set_tick_params(labelsize=12)
    ax.yaxis.set_tick_params(labelsize=12)


plt.tight_layout()

plt.show()
# plt.savefig("hessian_scaling.pdf")
