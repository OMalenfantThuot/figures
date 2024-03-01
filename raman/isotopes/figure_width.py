import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rc("text", usetex=True)
plt.rc("text.latex", preamble=r"\usepackage{bm}")

base_datadir = "data"

exp_data = pd.read_csv(os.path.join(base_datadir, "FWHM_exp.csv"))
width_data = {}
concentrations = np.arange(0, 1.01, 0.05)

data, errors = [], []

for c in concentrations:
    datadir = os.path.join(base_datadir, f"{c:.2f}")
    datafiles = [f for f in os.listdir(datadir) if f.endswith(".csv")]
    values = []
    for file in datafiles:
        values.append(pd.read_csv(os.path.join(datadir, file))["FWHM"])
    data.append(np.mean(values))
    errors.append(np.std(values))

fig, ax = plt.subplots(figsize=(8, 9))

ax.scatter(
    exp_data["concentration"], exp_data["width"], color="r", label="Experimental"
)
if 1 == 1:
    ax.errorbar(
        concentrations, data, yerr=errors, color="b", label="ML", ls="", marker="o"
    )

ax.legend(fontsize=20, loc="lower center")
ax.grid("on")
ax.set_xlim(-0.05, 1.05)
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set_xlabel(r"$^{13}$C concentration", fontsize=25)
ax.set_ylabel(r"G peak width (cm$^{-1}$)", fontsize=25)

plt.tight_layout()
# plt.show()
plt.savefig("width_full.pdf")
