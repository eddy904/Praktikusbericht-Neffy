"""Reichweitenmessung des Thermalsensors (D6T-1A-02) aus der Firmware-Aufzeichnung.

Eine Person hielt sich nacheinander in 3, 2, 1,5, 1 und 0,5 m Entfernung vor dem Roboter auf,
davor und danach war der Platz leer. Ausgewertet werden je Abschnitt die Erwärmung gegenüber
der gelernten Raumtemperatur (above_room_C) und der Anteil der Zeit mit Meldung
"Person da" (someone_there).

Aufruf (im Projektordner):  python daten/plot_thermal.py
Ausgabe: abbildungen/plots/thermal_reichweite.pdf und Tabelle auf der Konsole
"""
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

BASIS = Path(__file__).resolve().parent
DATEI = BASIS / "thermal-distance-261026-2137.csv"
AUSGABE = BASIS.parent / "abbildungen" / "plots"

SCHWELLE_K = 1.0  # ENTER_MIN_C in PersonSensor.cpp

FARBE_LINIE = "#2a78d6"
FARBE_TEXT = "#0b0b0b"
FARBE_GEDAEMPFT = "#52514e"
FARBE_RASTER = "#e2e1dc"

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
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.edgecolor": FARBE_GEDAEMPFT,
    "axes.labelcolor": FARBE_TEXT,
    "xtick.color": FARBE_GEDAEMPFT,
    "ytick.color": FARBE_GEDAEMPFT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": FARBE_RASTER,
    "grid.linewidth": 0.5,
})

KOMMA = FuncFormatter(lambda x, _: f"{x:g}".replace(".", "{,}"))


def abschnitte():
    d = pd.read_csv(DATEI)
    d["abschnitt"] = (d["distance"] != d["distance"].shift()).cumsum()
    return d.groupby("abschnitt").agg(
        entfernung=("distance", "first"),
        dauer_s=("t_ms", lambda t: (t.max() - t.min()) / 1000),
        dT_mittel=("above_room_C", "mean"),
        dT_min=("above_room_C", "min"),
        dT_max=("above_room_C", "max"),
        erkannt_anteil=("someone_there", "mean"),
    )


if __name__ == "__main__":
    t = abschnitte()
    print(t.round(2).to_string())

    p = t[t["entfernung"] != "away"].copy()
    p["d_m"] = p["entfernung"].str.replace(" m", "").astype(float)
    p = p.sort_values("d_m")

    fig, ax = plt.subplots(figsize=(10 / 2.54, 5.6 / 2.54))
    ax.vlines(p["d_m"], p["dT_min"], p["dT_max"], color=FARBE_LINIE, linewidth=1.0)
    ax.plot(p["d_m"], p["dT_mittel"], "o-", color=FARBE_LINIE, markersize=4, linewidth=1.0)
    for _, z in p.iterrows():
        ax.text(z["d_m"] + 0.06, z["dT_mittel"] + 0.12, f"{100 * z['erkannt_anteil']:.0f}\\,\\%",
                fontsize=7, color=FARBE_GEDAEMPFT)
    ax.axhline(SCHWELLE_K, color=FARBE_GEDAEMPFT, linewidth=0.6, linestyle=(0, (3, 2)))
    ax.text(0.05, SCHWELLE_K + 0.08, "Schwelle 1\\,K", ha="left", fontsize=7, color=FARBE_GEDAEMPFT)
    ax.set_xlim(0, 3.3)
    ax.set_ylim(0, 5)
    ax.xaxis.set_major_formatter(KOMMA)
    ax.yaxis.set_major_formatter(KOMMA)
    ax.set_xlabel("Entfernung in m")
    ax.set_ylabel("Erwärmung in K")
    fig.tight_layout(pad=0.3)
    AUSGABE.mkdir(parents=True, exist_ok=True)
    fig.savefig(AUSGABE / "thermal_reichweite.pdf")
    plt.close(fig)
    print("Diagramm gespeichert in", AUSGABE)
