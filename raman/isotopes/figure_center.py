import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.optimize import curve_fit

plt.rc("text", usetex=True)
plt.rc("text.latex", preamble=r"\usepackage{bm}")


def linearFunc(x, intercept, slope):
    y = intercept + slope * x
    return y


base_datadir = "data"

exp_data = pd.read_csv(os.path.join(base_datadir, "center_exp.csv"))
center_data = []
concentrations = np.arange(0, 1.01, 0.05)

data, errors = [], []

for c in concentrations:
    datadir = os.path.join(base_datadir, f"{c:.2f}")
    datafiles = [f for f in os.listdir(datadir) if f.endswith(".csv")]
    values = []
    for file in datafiles:
        values.append(pd.read_csv(os.path.join(datadir, file))["center"])
    data.append(np.mean(values))
    errors.append(np.std(values))

fig, ax = plt.subplots(figsize=(8, 9))

(inter, slope), cov = curve_fit(linearFunc, concentrations, data)
(inter_exp, slope_exp), cov_exp = curve_fit(
    linearFunc, exp_data["concentration"], exp_data["center"]
)
inter_error = np.sqrt(cov[0][0])
slope_error = np.sqrt(cov[1][1])
inter_error_exp = np.sqrt(cov_exp[0][0])
slope_error_exp = np.sqrt(cov_exp[1][1])

yfit = inter + slope * concentrations
yfit_exp = inter_exp + slope_exp * exp_data["concentration"]

ax.scatter(
    exp_data["concentration"], exp_data["center"], color="r", label="Experimental"
)
if 1 == 1:
    ax.plot(
        exp_data["concentration"],
        yfit_exp,
        label=f"Slope: ({slope_exp:3.1f}"
        + r" $\pm$ "
        + f"{slope_error_exp:2.1f})"
        + r" cm$^{-1}$",
        linestyle="--",
        color="r",
    )
    ax.errorbar(
        concentrations, data, yerr=errors, color="b", label="ML", ls="", marker="o"
    )
    ax.plot(
        concentrations,
        yfit,
        label=f"Slope: ({slope:3.1f}"
        + r" $\pm$ "
        + f"{slope_error:2.1f})"
        + r" cm$^{-1}$",
        linestyle="--",
        color="b",
    )

ax.legend(fontsize=20)
ax.grid("on")
ax.set_ylim([1490, 1595])
ax.xaxis.set_tick_params(labelsize=20)
ax.yaxis.set_tick_params(labelsize=20)
ax.set_xlabel(r"$^{13}$C concentration", fontsize=25)
ax.set_ylabel(r"G peak position (cm$^{-1}$)", fontsize=25)

plt.tight_layout()
# plt.show()
plt.savefig("center_full.pdf")
