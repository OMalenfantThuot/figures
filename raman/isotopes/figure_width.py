import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

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

ax.scatter(exp_data["concentration"], exp_data["width"], color="r", label="Experimental")
ax.errorbar(concentrations, data, yerr=errors, color="b", label="ML", ls="", marker="o")

ax.legend(fontsize=20)
ax.grid("on")
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set_xlabel("C13 concentration", fontsize=25)
ax.set_ylabel("G peak width", fontsize=25)

plt.tight_layout()
plt.show()
