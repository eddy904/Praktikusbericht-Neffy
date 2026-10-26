"""Theoretische Kennlinie des Spannungsteilers der Drucksensoren (Kap. 4.2).

U_A = U_B * R_F / (R_F + R_S)   (Sensor zwischen Versorgung und Messpunkt, R_F gegen Masse)
Keine Messdaten: berechnete Kurven für verschiedene Festwiderstände R_F.

Aufruf (im Projektordner):  python daten/plot_spannungsteiler.py
Ausgabe: abbildungen/plots/spannungsteiler.pdf
"""
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

AUSGABE = Path(__file__).resolve().parent.parent / "abbildungen" / "plots" / "spannungsteiler.pdf"

U_B = 3.3          # Versorgung des Teilers in V
U_SAETTIGUNG = 3.1  # ADC des ESP32-S3 bei 11 dB laut Firmware-Kommentar (VoltageReader.cpp)

FARBE_LINIE = "#2a78d6"
FARBE_TEXT = "#0b0b0b"
FARBE_GEDAEMPFT = "#52514e"
FARBE_GRAU = "#9a9993"
FARBE_RASTER = "#e2e1dc"
FARBE_BAND = "#f1efe8"

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
    "pgf.preamble": "\n".join([
        r"\usepackage[T1]{fontenc}",
        r"\usepackage[utf8]{inputenc}",
        r"\usepackage{lmodern}",
    ]),
    "font.family": "serif",
    "font.size": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.edgecolor": FARBE_GEDAEMPFT,
    "axes.labelcolor": FARBE_TEXT,
    "xtick.color": FARBE_GEDAEMPFT,
    "ytick.color": FARBE_GEDAEMPFT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": FARBE_RASTER,
    "grid.linewidth": 0.5,
})

r_s = np.logspace(2, 6, 400)  # Sensorwiderstand 100 Ohm ... 1 MOhm

fig, ax = plt.subplots(figsize=(12.5 / 2.54, 6.4 / 2.54))

# FSR-Schaltschwelle laut Interlink: von > 100 kOhm auf etwa 10 kOhm
ax.axvspan(1e4, 1e5, color=FARBE_BAND, zorder=0)
ax.text(np.sqrt(1e4 * 1e5), 0.08, "FSR-Schalt-\nschwelle",
        ha="center", va="bottom", fontsize=7, color=FARBE_GEDAEMPFT)

# (R_F, Name, Farbe, Linienstärke, Höhe der Beschriftung in V) – Beschriftungen gestaffelt
kurven = [(100e3, "100 k$\\Omega$", FARBE_GRAU, 1.0, 2.75),
          (10e3, "10 k$\\Omega$", FARBE_LINIE, 1.6, 2.15),
          (4.7e3, "4,7 k$\\Omega$", FARBE_GRAU, 1.0, 1.45),
          (1e3, "1 k$\\Omega$", FARBE_GRAU, 1.0, 0.8)]
for r_f, name, farbe, breite, u_text in kurven:
    u = U_B * r_f / (r_f + r_s)
    ax.plot(r_s, u, color=farbe, linewidth=breite)
    # Punkt bei R_S = R_F: dort ist der Teiler am empfindlichsten (U_A = U_B/2)
    ax.plot([r_f], [U_B / 2], "o", markersize=3.5, color=farbe, markeredgecolor="white", markeredgewidth=0.6)
    # Beschriftung neben der Kurve auf der Höhe u_text; 10 kOhm links davon, damit sie
    # nicht an der nahen 4,7-kOhm-Kurve steht (x-Achse ist invertiert)
    x_text = r_f * (U_B / u_text - 1.0)
    if r_f == 10e3:
        ax.text(x_text * 1.35, u_text, r"$R_\mathrm{F}$ = " + name, fontsize=7, color=FARBE_TEXT,
                va="center", ha="right")
    else:
        ax.text(x_text / 1.35, u_text, r"$R_\mathrm{F}$ = " + name, fontsize=7, color=FARBE_TEXT, va="center")

ax.axhline(U_SAETTIGUNG, color=FARBE_GEDAEMPFT, linewidth=0.6, linestyle=(0, (3, 2)))
ax.text(9e5, U_SAETTIGUNG + 0.05, "Sättigung des ADC (ca. 3,1 V)", fontsize=7, color=FARBE_GEDAEMPFT,
        va="bottom", ha="left")

ax.set_xscale("log")
ax.set_xlim(1e2, 1e6)
ax.set_ylim(0, 3.6)
ax.set_xticks([1e2, 1e3, 1e4, 1e5, 1e6])
ax.set_xticklabels(["100 $\\Omega$", "1 k$\\Omega$", "10 k$\\Omega$", "100 k$\\Omega$", "1 M$\\Omega$"])
ax.set_yticks([0, 1, 2, 3])
ax.set_xlabel(r"Sensorwiderstand $R_\mathrm{S}$ (sinkt mit steigendem Druck)")
ax.set_ylabel(r"$U_\mathrm{A}$ in V")
ax.invert_xaxis()  # links wenig Druck (hoher Widerstand), rechts viel Druck

fig.tight_layout(pad=0.3)
AUSGABE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(AUSGABE)
print("geschrieben:", AUSGABE)
