"""Erzeugt das Kennwerte-Diagramm der Atemsensorik für Kap. 5 aus der Übersichtstabelle.

Aufruf (im Projektordner):  python daten/plot_kennwerte.py
Quelle:  daten/Messdaten_Atemsensorik/00_Uebersicht_Kennwerte.csv
Ausgabe: abbildungen/plots/kennwerte_atemsensorik.pdf
Stil wie daten/plots_atemsensorik.py (Schrift über pdflatex).
"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("pgf")
import matplotlib.pyplot as plt  # noqa: E402

BASIS = Path(__file__).resolve().parent
QUELLE = BASIS / "Messdaten_Atemsensorik" / "00_Uebersicht_Kennwerte.csv"
AUSGABE = BASIS.parent / "abbildungen" / "plots" / "kennwerte_atemsensorik.pdf"

FARBE_LINIE = "#2a78d6"      # Zwischenbereich / Signalhub (wie die Messkurven)
FARBE_NULL = "#c9c8c2"       # Wert 0: Sensor meldet „aus“
FARBE_VOLL = "#52514e"       # Wert 4095: Sensor meldet „voll“
FARBE_RAND = "#a9c8ef"       # knapp über 0 bzw. knapp unter 4095
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
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.edgecolor": FARBE_GEDAEMPFT,
    "axes.labelcolor": FARBE_TEXT,
    "xtick.color": FARBE_GEDAEMPFT,
    "ytick.color": FARBE_GEDAEMPFT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.grid.axis": "x",
    "grid.color": FARBE_RASTER,
    "grid.linewidth": 0.5,
})


def zahl(text):
    text = text.strip()
    return float(text.replace(",", ".")) if text else None


def frequenz(text):
    """'4,22 s / 14,2 /min' -> 14.2"""
    return zahl(text.split("/")[1].strip().split(" ")[0]) if "/" in text else None


def komma(x, stellen=1):
    return f"{x:.{stellen}f}".replace(".", "{,}")


with open(QUELLE, encoding="utf-8-sig", newline="") as f:
    reihen = list(csv.DictReader(f, delimiter=";"))

# y-Positionen von oben nach unten, mit Abstand zwischen den Gruppen
positionen, gruppen, y, vorher = [], {}, 0.0, None
for r in reihen:
    if vorher is not None and r["Gruppe"] != vorher:
        y += 0.8
    positionen.append(y)
    gruppen.setdefault(r["Gruppe"], []).append(y)
    vorher = r["Gruppe"]
    y += 1.0

ids = [r["ID"] for r in reihen]
null = [zahl(r["Anteil_Null_%"]) for r in reihen]
voll = [zahl(r["Anteil_Saettigung_4095_%"]) for r in reihen]
mitte = [zahl(r["Anteil_Zwischenbereich_100-4000_%"]) for r in reihen]
# Werte 1-99 und 4001-4094 gehören zu keiner der drei Klassen der Quelle
randwerte = [max(100.0 - n - m - v, 0.0) for n, m, v in zip(null, mitte, voll)]
hub = [zahl(r["Signalhub_P95-P5_ADC"]) for r in reihen]
f_atem = [frequenz(r["Mittl_Atemperiode / Atemfrequenz"]) for r in reihen]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0 / 2.54, 7.2 / 2.54), sharey=True,
                               gridspec_kw={"width_ratios": [1.15, 1.0], "wspace": 0.08})
hoehe = 0.72
rand = dict(edgecolor="white", linewidth=0.8)

# (a) Anteile: 0 | Zwischenbereich | Sättigung
links = [0.0] * len(reihen)
for werte, farbe, name in [(null, FARBE_NULL, "0 (aus)"),
                           (randwerte, FARBE_RAND, "1--99 bzw. 4001--4094"),
                           (mitte, FARBE_LINIE, "100--4000 (abgestuft)"),
                           (voll, FARBE_VOLL, "4095 (voll)")]:
    ax1.barh(positionen, werte, left=links, height=hoehe, color=farbe, label=name, **rand)
    links = [l + w for l, w in zip(links, werte)]
ax1.set_xlim(0, 100)
ax1.set_xticks([0, 25, 50, 75, 100])
ax1.set_xlabel(r"Anteil der Messwerte in \%")
ax1.set_title("(a) Verteilung der Messwerte", loc="left", fontsize=9, color=FARBE_TEXT)
ax1.legend(loc="upper left", bbox_to_anchor=(-0.2, -0.2), ncol=4, frameon=False,
           fontsize=7, handlelength=1.2, columnspacing=1.0, title="Messwerte (ADC):",
           title_fontsize=7, alignment="left")

# (b) Signalhub, Atemfrequenz als Beschriftung
for yy, h, fa in zip(positionen, hub, f_atem):
    if h is None:
        ax2.text(60, yy, "nicht bestimmt", va="center", fontsize=7, color=FARBE_GEDAEMPFT)
        continue
    ax2.barh(yy, h, height=hoehe, color=FARBE_LINIE, **rand)
    if fa is not None:
        ax2.text(h + 60, yy, komma(fa) + r"\,/min", va="center", fontsize=7, color=FARBE_TEXT)
    else:
        ax2.text(h + 60, yy, "keine Atemzüge", va="center", fontsize=7, color=FARBE_GEDAEMPFT)
ax2.set_xlim(0, 4300)
ax2.set_xticks([0, 1000, 2000, 3000, 4000])
ax2.set_xlabel("Signalhub in ADC-Einheiten (P95 -- P5)")
ax2.set_title("(b) Signalhub und Atemfrequenz", loc="left", fontsize=9, color=FARBE_TEXT)

ax1.set_yticks(positionen)
ax1.set_yticklabels(ids)
ax1.invert_yaxis()
ax1.tick_params(axis="y", length=0)
ax2.tick_params(axis="y", length=0)

# Gruppennamen links neben den IDs
namen = {"FSR": "FSR", "Velostat aufgelegt": "Velostat,\naufgelegt", "Velostat aktiv": "Velostat,\naktiv"}
for gruppe, ys in gruppen.items():
    ax1.text(-17, sum(ys) / len(ys), namen.get(gruppe, gruppe), ha="right", va="center",
             fontsize=8, color=FARBE_TEXT, linespacing=1.1)

fig.subplots_adjust(left=0.2, right=0.98, top=0.92, bottom=0.27)
AUSGABE.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(AUSGABE)
print("geschrieben:", AUSGABE)
