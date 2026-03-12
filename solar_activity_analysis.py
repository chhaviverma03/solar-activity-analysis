import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("SN_m_tot_V2.0.csv", sep=";", header=None)

data.columns = ["year","month","date","sunspot","std","obs","def"]

data["year"] = pd.to_numeric(data["year"])
data["month"] = pd.to_numeric(data["month"])
data["sunspot"] = pd.to_numeric(data["sunspot"])

data["time"] = data["year"] + data["month"]/12

plt.figure(figsize=(10,5))
plt.plot(data["time"], data["sunspot"])
plt.xlabel("Year")
plt.ylabel("Sunspot Number")
plt.title("Solar Activity Over Time")
plt.grid()

plt.savefig("solar_activity_plot.png")
plt.show()

sunspot = data["sunspot"].values

# remove mean
sunspot = sunspot - np.mean(sunspot)

# FFT
fft_vals = np.fft.fft(sunspot)
freqs = np.fft.fftfreq(len(sunspot))

plt.figure(figsize=(10,5))
plt.plot(freqs[1:200], np.abs(fft_vals[1:200]))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Frequency Spectrum of Solar Activity")
plt.grid()

plt.savefig("solar_fft_spectrum.png")
plt.show()
