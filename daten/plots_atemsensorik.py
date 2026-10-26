"""Erzeugt die Diagramme der Atemsensorik direkt aus den CSV-Dateien.

Aufruf (im Projektordner):  python daten/plots_atemsensorik.py
Ausgabe: abbildungen/plots/*.pdf  (Schrift über pdflatex, passend zum Bericht)
"""
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

BASIS = Path(__file__).resolve().parent
DATEN = BASIS / "Messdaten_Atemsensorik"
AUSGABE = BASIS.parent / "abbildungen" / "plots"

U_MAX = 3.3  # ADC 4095 entspricht 3,3 V (siehe LIESMICH.txt)

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
    "lines.linewidth": 1.0,
})

# Dezimalkomma auf den Achsen
KOMMA = FuncFormatter(lambda x, _: f"{x:g}".replace(".", "{,}"))


def lies(datei):
    # index_col=False: Die Bemerkung zu A6 in der Übersicht enthält ein Semikolon und damit
    # ein Feld zu viel; ohne diese Option würde pandas die ID-Spalte zum Index machen.
    return pd.read_csv(DATEN / datei, sep=";", decimal=",", encoding="utf-8-sig",
                       index_col=False)


def reihe(tabelle, kennung):
    t = tabelle[f"{kennung}_Zeit_s"]
    u = tabelle[f"{kennung}_Spannung_V"]
    gueltig = t.notna() & u.notna()
    return t[gueltig].to_numpy(), u[gueltig].to_numpy()


def peaks(kennung):
    """Peak-Zeitpunkte aus der Kennwert-Übersicht (Spalte 'Peak-Zeitpunkte_s')."""
    uebersicht = lies("00_Uebersicht_Kennwerte.csv").set_index("ID")
    eintrag = uebersicht.loc[kennung, "Peak-Zeitpunkte_s"]
    if pd.isna(eintrag):
        return []
    return [float(s.strip().replace(",", ".")) for s in str(eintrag).split("|")]


def achse_einrichten(ax, t_max, saettigung=True):
    ax.set_xlim(0, t_max)
    ax.set_ylim(0, 3.5)
    ax.set_yticks([0, 1, 2, 3])
    ax.xaxis.set_major_formatter(KOMMA)
    ax.yaxis.set_major_formatter(KOMMA)
    ax.set_xlabel("Zeit in s")
    ax.set_ylabel("Spannung in V")
    if saettigung:
        ax.axhline(U_MAX, color=FARBE_GEDAEMPFT, linewidth=0.6, linestyle=(0, (3, 2)))
        ax.text(t_max, U_MAX + 0.06, "Sättigung (ADC 4095)", ha="right", va="bottom",
                fontsize=7, color=FARBE_GEDAEMPFT)


def kurve(ax, t, u, kennung, peaks_markieren=False):
    ax.plot(t, u, color=FARBE_LINIE)
    if peaks_markieren:
        for tp in peaks(kennung):
            i = abs(t - tp).argmin()
            ax.plot(t[i], u[i], "o", markersize=4, color=FARBE_LINIE,
                    markeredgecolor="white", markeredgewidth=0.8)


def einzelplot(datei, kennung, name, t_max=None):
    t, u = reihe(lies(datei), kennung)
    fig, ax = plt.subplots(figsize=(7.4 / 2.54, 4.8 / 2.54))
    kurve(ax, t, u, kennung)
    achse_einrichten(ax, t_max or t.max())
    fig.tight_layout(pad=0.3)
    fig.savefig(AUSGABE / name)
    plt.close(fig)


def vergleich_aufgelegt_aktiv(name):
    """Kap. 5: Hände nur aufgelegt (P2) gegenüber aktivem Mitdrücken (A5)."""
    t_p, u_p = reihe(lies("2_Velostat_aufgelegt.csv"), "P2")
    t_a, u_a = reihe(lies("3_Velostat_aktiv.csv"), "A5")
    t_max = max(t_p.max(), t_a.max())
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15 / 2.54, 8.5 / 2.54), sharex=True)
    kurve(ax1, t_p, u_p, "P2")
    achse_einrichten(ax1, t_max)
    ax1.set_xlabel("")
    ax1.set_title("(a) Hände nur aufgelegt (P2)", loc="left", fontsize=9, color=FARBE_TEXT)
    kurve(ax2, t_a, u_a, "A5", peaks_markieren=True)
    achse_einrichten(ax2, t_max)
    ax2.set_title("(b) Aktives Mitdrücken beim Einatmen (A5), Punkte = erkannte Atemzüge",
                  loc="left", fontsize=9, color=FARBE_TEXT)
    fig.tight_layout(pad=0.3)
    fig.savefig(AUSGABE / name)
    plt.close(fig)


def vergleich_drei(name):
    """Kap. 4/5: FSR (F1), Velostat aufgelegt (P2) und Velostat aktiv (A5) nebeneinander."""
    reihen = [("1_FSR.csv", "F1", "(a) FSR (F1)", False),
              ("2_Velostat_aufgelegt.csv", "P2", "(b) Velostat, aufgelegt (P2)", False),
              ("3_Velostat_aktiv.csv", "A5", "(c) Velostat, aktiv (A5)", True)]
    fig, achsen = plt.subplots(1, 3, figsize=(15 / 2.54, 5.2 / 2.54), sharey=True)
    for ax, (datei, kennung, titel, mit_peaks) in zip(achsen, reihen):
        t, u = reihe(lies(datei), kennung)
        kurve(ax, t, u, kennung, peaks_markieren=mit_peaks)
        achse_einrichten(ax, t.max(), saettigung=False)
        ax.axhline(U_MAX, color=FARBE_GEDAEMPFT, linewidth=0.6, linestyle=(0, (3, 2)))
        ax.set_title(titel, loc="left", fontsize=8, color=FARBE_TEXT)
        if ax is not achsen[0]:
            ax.set_ylabel("")
    fig.tight_layout(pad=0.3, w_pad=0.8)
    fig.savefig(AUSGABE / name)
    plt.close(fig)


def alle_reihen(name):
    """Anhang B: alle elf Messreihen im Überblick (F1-F3, P1-P2, A1-A6)."""
    gruppen = [("1_FSR.csv", ["F1", "F2", "F3"]),
               ("2_Velostat_aufgelegt.csv", ["P1", "P2"]),
               ("3_Velostat_aktiv.csv", ["A1", "A2", "A3", "A4", "A5", "A6"])]
    reihen = [(datei, k) for datei, ks in gruppen for k in ks]
    fig, achsen = plt.subplots(4, 3, figsize=(15 / 2.54, 17 / 2.54), sharey=True)
    for ax, (datei, kennung) in zip(achsen.flat, reihen):
        t, u = reihe(lies(datei), kennung)
        kurve(ax, t, u, kennung)
        achse_einrichten(ax, t.max(), saettigung=False)
        ax.axhline(U_MAX, color=FARBE_GEDAEMPFT, linewidth=0.6, linestyle=(0, (3, 2)))
        ax.set_title(kennung, loc="left", fontsize=8, color=FARBE_TEXT)
        ax.set_xlabel("Zeit in s", fontsize=7)
        ax.set_ylabel("U in V" if ax in achsen[:, 0] else "", fontsize=7)
    achsen.flat[-1].set_visible(False)
    fig.tight_layout(pad=0.3, h_pad=0.6, w_pad=0.6)
    fig.savefig(AUSGABE / name)
    plt.close(fig)


if __name__ == "__main__":
    AUSGABE.mkdir(parents=True, exist_ok=True)
    einzelplot("1_FSR.csv", "F1", "fsr_F1.pdf")
    einzelplot("3_Velostat_aktiv.csv", "A5", "velostat_aktiv_A5.pdf")
    vergleich_aufgelegt_aktiv("velostat_aufgelegt_vs_aktiv.pdf")
    vergleich_drei("vergleich_F1_P2_A5.pdf")
    alle_reihen("alle_messreihen.pdf")
    print("Diagramme gespeichert in", AUSGABE)
