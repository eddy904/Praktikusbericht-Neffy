"""Erzeugt die Kennwerte-Tabelle der Atemsensorik für Kap. 5 als LaTeX-Datei.

Liest daten/Messdaten_Atemsensorik/00_Uebersicht_Kennwerte.csv (Semikolon, Dezimalkomma)
und schreibt daten/tab_kennwerte.tex. Aufruf aus dem Projektordner:
    python daten/tabelle_kennwerte.py
"""
import csv
from pathlib import Path

ORDNER = Path(__file__).resolve().parent
QUELLE = ORDNER / "Messdaten_Atemsensorik" / "00_Uebersicht_Kennwerte.csv"
ZIEL = ORDNER / "tab_kennwerte.tex"

GRUPPE = {"FSR": r"\acs{FSR}", "Velostat aufgelegt": "Velostat, aufgelegt",
          "Velostat aktiv": "Velostat, aktiv"}


def zahl(text):
    """Dezimalkomma -> LaTeX-Zahl mit {,}; leer -> Strich."""
    text = text.strip()
    return text.replace(",", "{,}") if text else "--"


def frequenz(text):
    """'4,22 s / 14,2 /min' -> '14{,}2'; leer -> Strich."""
    if "/" not in text:
        return "--"
    return zahl(text.split("/")[1].strip().split(" ")[0])


with open(QUELLE, encoding="utf-8-sig", newline="") as f:
    zeilen = list(csv.DictReader(f, delimiter=";"))

ausgabe = [
    "% Automatisch erzeugt von daten/tabelle_kennwerte.py -- nicht von Hand bearbeiten",
    r"\begin{tabular}{@{}l l r r r r r c r@{}}",
    r"  \toprule",
    r"  & & Dauer & \multicolumn{3}{c}{Anteil der Messwerte in \%} & Signal- & Atem- & Atem- \\",
    r"  \cmidrule(lr){4-6}",
    r"  ID & Aufbau & in s & bei 0 & bei 4095 & 100--4000 & hub & züge & frequenz \\",
    r"  & & & & & & (ADC) & & (1/min) \\",
    r"  \midrule",
]
vorher = None
for z in zeilen:
    if vorher is not None and z["Gruppe"] != vorher:
        ausgabe.append(r"  \addlinespace")
    vorher = z["Gruppe"]
    ausgabe.append("  " + " & ".join([
        z["ID"], GRUPPE.get(z["Gruppe"], z["Gruppe"]), zahl(z["Dauer_s"]),
        zahl(z["Anteil_Null_%"]), zahl(z["Anteil_Saettigung_4095_%"]),
        zahl(z["Anteil_Zwischenbereich_100-4000_%"]), zahl(z["Signalhub_P95-P5_ADC"]),
        zahl(z["Atemzyklen_erkannt"]), frequenz(z["Mittl_Atemperiode / Atemfrequenz"]),
    ]) + r" \\")
ausgabe += [r"  \bottomrule", r"\end{tabular}", ""]

ZIEL.write_text("\n".join(ausgabe), encoding="utf-8")
print(f"{len(zeilen)} Messreihen -> {ZIEL}")
