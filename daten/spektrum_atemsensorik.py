"""Spektrale Auswertung der Velostat-Messreihen (P1, P2, A1-A6) im Atemband.

Je Messreihe: staerkste Frequenz im Atemband 0,1-0,5 Hz (6-30 Atemzuege/min) sowie der
Effektivwert (RMS) des Signals im Atemband und oberhalb davon (> 0,5 Hz, Rauschen und
schnelle Bewegungen). Ausgewertet wird dasselbe Auswertefenster wie bei den Kennwerten
(00_Uebersicht_Kennwerte.csv); vorher wird ein linearer Trend entfernt.

Aufruf: python daten/spektrum_atemsensorik.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATEN = Path(__file__).parent / "Messdaten_Atemsensorik"
BAND = (0.1, 0.5)  # Hz


def fenster(text):
    a, b = str(text).replace(",", ".").replace("–", "-").split("-")
    return float(a), float(b)


uebersicht = pd.read_csv(DATEN / "00_Uebersicht_Kennwerte.csv", sep=";", decimal=",",
                         encoding="utf-8-sig", index_col=False)
werte = pd.read_csv(DATEN / "99_Alle_Messwerte_Langformat.csv", sep=";", decimal=",",
                    encoding="utf-8-sig", index_col=False)

print(f"{'ID':4} {'Fenster s':>10} {'Max. /min':>9} {'RMS Atemband':>12} {'RMS > 0,5 Hz':>12}")
for _, z in uebersicht.iterrows():
    if not str(z["ID"]).startswith(("P", "A")):
        continue
    t0, t1 = fenster(z["Auswertefenster_s"])
    r = werte[(werte["ID"] == z["ID"]) & (werte["Zeit_s"] >= t0) & (werte["Zeit_s"] <= t1)]
    x = r["ADC"].to_numpy(dtype=float)
    dt = z["Abtastintervall_ms"] / 1000
    n = np.arange(len(x))
    x = x - np.polyval(np.polyfit(n, x, 1), n)          # linearen Trend entfernen

    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), dt)
    im_band = (f >= BAND[0]) & (f <= BAND[1])
    rms_band = np.fft.irfft(np.where(im_band, X, 0), n=len(x)).std()
    rms_rest = np.fft.irfft(np.where(f > BAND[1], X, 0), n=len(x)).std()

    # Lage des Maximums mit Hann-Fenster und Nullauffuellung fuer ein feineres Raster
    p = np.abs(np.fft.rfft(x * np.hanning(len(x)), n=8 * len(x))) ** 2
    f8 = np.fft.rfftfreq(8 * len(x), dt)
    k = np.argmax(np.where((f8 >= BAND[0]) & (f8 <= BAND[1]), p, 0))

    print(f"{z['ID']:4} {t0:4.1f}-{t1:4.1f} {60 * f8[k]:9.1f} {rms_band:12.0f} {rms_rest:12.0f}")
