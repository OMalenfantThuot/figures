# This code generates a plot of raman spectra for 50x50 hBN sc with different B vacancies concentrations.
# Note that the concentraion is calculated using number_vac/number_of_B_and_N_sites

import numpy as np
import matplotlib.pyplot as plt

plt.rc("text", usetex=True)
plt.rc("text.latex", preamble=r"\usepackage{bm}")

data_50x50_0percent_relaxed = np.loadtxt("raman50x50_0percent_w3_npts_2000_relaxed.dat")
data_50x50_0p5percent_relaxed = np.loadtxt(
    "raman50x50_0p5percent_w3_npts_2000_relaxed.dat"
)
data_50x50_1percent_relaxed = np.loadtxt("raman50x50_1percent_w3_npts_2000_relaxed.dat")
data_50x50_2percent_relaxed = np.loadtxt("raman50x50_2percent_w3_npts_2000_relaxed.dat")

fig, rdosax = plt.subplots(figsize=(8, 10))

shift = 0.2

rdosax.plot(
    data_50x50_0percent_relaxed[:, 0],
    data_50x50_0percent_relaxed[:, 1],
    label="0.0\%",
)
rdosax.plot(
    data_50x50_0p5percent_relaxed[:, 0],
    data_50x50_0p5percent_relaxed[:, 1] + 1 * shift,
    label="0.5\%",
)
rdosax.plot(
    data_50x50_1percent_relaxed[:, 0],
    data_50x50_1percent_relaxed[:, 1] + 2 * shift,
    label="1.0\%",
)
rdosax.plot(
    data_50x50_2percent_relaxed[:, 0],
    data_50x50_2percent_relaxed[:, 1] + 3 * shift,
    label="2.0\%",
)
rdosax.plot([1368.6, 1384.9], [0.2115, 0.6606], ls="--", color="k")

rdosax.grid("on")
rdosax.set_xlim(1200, 1550)
rdosax.set_ylim(0, 0.85)
rdosax.set_title("Raman Spectra, hBN with B vacancies.", fontsize=20)
rdosax.set_xlabel("Frequency (cm$^{-1}$)", fontsize=20)
rdosax.set_ylabel("Relative Intensity", fontsize=20)
rdosax.xaxis.set_tick_params(labelsize=15)
rdosax.yaxis.set_tick_params(labelsize=15)
plt.legend(
    loc="upper left", fontsize=16, title="Vacancies\nconcentration", title_fontsize=20
)
plt.tight_layout()

# plt.show()
plt.savefig("raman_hBN_B_vacancies.pdf")
