# Analyse: Firmware Neffy 3.0 Mainboard

- Repo: https://github.com/YounesJamil/Neffy-3.0-Mainboard. Gelesener Stand: Commit `2693747`
  vom 21.10.2026, 19:02, Autor im Git-Log: Younes Jamil.
- UART-Bibliothek: https://github.com/LegitimateShake/Neffy_UART_Interface, Commit `f315d6b`
  (fest in `platformio.ini`). Darin `Supported_Commands.h` und `docs/Neffy Interface Commands.pdf`.

## Hardware laut Code (`config.h`)
| Teil | Angabe im Code |
|---|---|
| Mikrocontroller | ESP32-S3 („Mainboard“, eigene Board-Definition), Arduino-Framework, PlatformIO |
| Anwesenheit | Omron D6T, Einzelpixel (D6T-1A, genaue Variante -01/-02 nicht im Code), I²C 100 kHz, alle 100 ms gelesen |
| Taschen | 2 Velostat-Drucksensoren, ADC 12 bit, 11 dB, eFuse-kalibriert, Mittel aus 8 Werten, alle 20 ms |
| Körper-Achse | Schrittmotor, **Gewindespindel 8 mm Steigung**, Hub **85 mm**, Referenzfahrt gegen Endschalter |
| Kopf-Achse | Schrittmotor, Zahnräder 30 → 40 Zähne, ca. 34° mechanisch, **32° genutzt** |
| Treiber | TMC2225, 4 Mikroschritte (auf der Platine fest eingestellt) |
| LEDs | WS2812B: je 8 unter jeder Tasche, Ring mit 12 LEDs; warmes Gelb; Helligkeit folgt dem Kopf |
| Sonstiges | Lautsprecher-Stummschaltung (MUTE) |
| Aufteilung | Motoren auf Kern 0, UART/Sensoren/LEDs auf Kern 1 (Schrittmotor-Interrupt mit 50 kHz und FastLED vertragen sich nicht auf einem Kern) |

Vergleich zu Neffy 2: Dort war es ein Riementrieb mit max. 25 mm Hub und Dynamixel-Motoren.
In Neffy 3.0 sind es Gewindespindel und Schrittmotoren mit 85 mm Hub.

## Erkennungsverfahren
**Anwesenheit (`PersonSensor.cpp`)**
- Eine Person gilt als da, sobald die Messung mindestens max(8 × Rauschen; 1 °C) über der gelernten
  Raumtemperatur liegt. Sie gilt als weg unter 60 % dieser Schwelle (Hysterese).
- Kommentar im Code: direkt davor +4 bis 6 °C, in 1 m Entfernung etwa +2 °C.
- Die Raumtemperatur wird adaptiv gelernt (verschiedene Zeitkonstanten von 1 bis 300 s). Als
  Sicherheitsnetz wird sie neu gelernt, wenn „Person da“ angezeigt wird, das Signal aber 20 s lang flach ist.
- Prüfsumme (CRC-8) für jede I²C-Messung.
- Parameter laut Kommentar „offline an einer geführten Aufnahme abgestimmt“ (`tools/thermal_log.py`:
  leerer Raum, Annähern, Davorstehen, 1 m, Vorbeigehen, Weggehen).
- Senden: bei jeder Änderung und zusätzlich alle 500 ms.

**Taschen/Klicks (`PressureDetector.cpp`)**
- Selbstkalibrierend: lernt Ruhepegel, Rauschen und typische Klickhöhe, weil die Sensoren driften.
- Klick = kurzer Puls (≤ 600 ms) oder schneller Sprung in beide Richtungen (leichte Klicks).
- Erkennt eine aufliegende Hand. Klicks unter der Hand müssen dann deutlicher sein.
- `pressed()` für die Atmung: reagiert nach 140 ms Drücken und 200 ms Loslassen.
- Parameter laut Kommentar „offline an aufgezeichneten Taschen-Logs abgestimmt“ (`tools/pocket_log.py`).

**Atemerkennung (`BreathingDetection.cpp`)**
- Startet auf Befehl und läuft **30 s** (nicht 20 s). Drücken = Einatmen.
- Die Atemfrequenz kommt aus der mittleren Zeit zwischen den Einatemzügen und wird hochgerechnet auf 30 s.
- Einstufung: ≤ 5 Atemzüge pro 30 s = entspannt, 6–10 = normal, mehr = gestresst.
  Begründung im Code: Erwachsene atmen in Ruhe 12–20-mal pro Minute. **Dafür brauchen wir eine Quelle.**
- An den Pi geht nur die Einstufung (RELAXED/NORMAL/STRESSED), weder Ein- und Ausatemdauer noch die
  Frequenz. `BREATHING_RATE` steht im Protokoll, wird aber nicht benutzt.

## UART-Protokoll
115200 Baud, Rahmen `FA <ID> <Länge> <Nutzdaten>`, höherwertiges Byte zuerst.
Werte werden mit Faktor 10 als ganze Zahl übertragen (mm, °, s).

| Gruppe | Pi → ESP32 | ESP32 → Pi |
|---|---|---|
| Bewegung | MOVE_BODY / MOVE_HEAD / MOVE_BODY_HEAD_IN_TIME (Ziel + Dauer) | Bestätigung mit erreichter Position |
| Anwesenheit | – | GET_PERSON_READING (0/1) |
| Taschen | – | PRESSURE_CLICK_L / _R |
| Atmung | BREATHING_DETECTION_START | _RELAXED / _NORMAL / _STRESSED |
| Sonstiges | MUTE; DISABLE_MOTORS (zweckentfremdet, s. u.) | – |

## Auffälligkeiten (für Diskussion/Schwachstellen)
- `DISABLE_MOTORS` schaltet die Motoren nicht ab. Der Befehl dient als Signal: Einmal gesendet
  verzögert er die nächste Bewegung um 0,5 s (Abgleich mit der Bildschirmanimation), zweimal gesendet
  hebt er die Verzögerung auf. Der Name passt also nicht zur Bedeutung.
- Probleme bei der Referenzfahrt sind im Code dokumentiert:
  - Stand die Achse beim Start schon auf dem Endschalter, fuhr sie in den Anschlag und verlor Schritte.
  - Beim Kopf blieb der Schalter bei zu kleinem Rückzug gedrückt, die Referenzfahrt hing in einer Endlosschleife.
  → Material für die Probleme mit den Schrittmotoren im Fazit.
- Die Aufnahmen zum Abstimmen (`logs/*.csv`) sind per `.gitignore` vom Repo ausgeschlossen. **Das sind
  unsere Messdaten. Sie liegen nur lokal bei dem, der sie aufgenommen hat.**
- `.gitignore` enthält `.claude/`. Das deutet auf Claude Code bei der Firmware-Entwicklung hin. Das
  muss im Bericht transparent genannt werden (Abschnitt KI-Nutzung).

## Zuordnung zu den Kapiteln
- Kap. 4 Systemarchitektur: Blockdiagramm, Kernaufteilung, UART-Tabelle, Sequenzdiagramm.
- Kap. 4 Hardware: Taschen, Thermalsensor, Spindel, Zahnräder, LEDs.
- Kap. 4 Software: die drei Erkennungsverfahren; Repo, Build, Debug-Werkzeuge, Hardwaretests.
- Kap. 5: Auswertung der Logs (Thermal: Temperaturdifferenz nach Entfernung; Taschen: Klick- und Druckverlauf).
- Anhang: `Supported_Commands.h`, Ausschnitte der Erkennungsverfahren.
