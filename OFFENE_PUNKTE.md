# Offene Punkte

## Material
- [x] Praxisbericht Neffy 2 liegt in `referenz/` → Analyse: `notizen/analyse_praxisbericht_neffy2.md`
- [x] BHT-Grafik fürs Titelblatt (`abbildungen/bht_titelseite.pdf`)
- [ ] Bericht zu Neffy 1 (Dincel & Thomas, 2024) beschaffen
- [x] Notiz `notizen/Notitzen_Sensoren.txt` gesichtet (Recherche, Testreihenfolge, Messreihen)
- [x] Atemkurven liegen in `daten/Messdaten_Atemsensorik/` (F1–F3 FSR, P1–P2 aufgelegt, A1–A6 aktiv, 50/200 ms, April 2026)
  - [x] P1/P2 = Hände nur aufgelegt (bestätigt 21.10.2026)
  - [x] A3 (Atemkurve 7): zu fest gedrückt, kein falscher Widerstand (bestätigt 21.10.2026)
  - [x] Messaufbau: ESP32-Entwicklungsboard, nicht Neffy Board (bestätigt, steht in Kap. 4.2)
  - [x] Plots erzeugt: `daten/plots_atemsensorik.py` → `abbildungen/plots/` (F1, A5 in Kap. 4; P2 vs. A5 für Kap. 5)
  - [x] FSR: mehrere Festwiderstände (1 kΩ … 100 kΩ) probiert, Verhalten immer binär → Spannungsteiler nicht die Ursache (Kap. 4.2)
  - [ ] Festwiderstand auf dem Neffy Board ebenfalls 10 kΩ? (klärt sich mit dem Schaltplan)
- [ ] **Ursprüngliche Liste Messdaten (Abgleich):**
  - `atemkurve_1_kleiner Drucksensor.csv`, `atemkurve_2_kleiner Drucksensor.csv` (FSR)
  - `atemkurve_3_Velostat.csv`, `atemkurve_4_Velostat ohne mitbewegen.csv` (passiv)
  - `atemkurve_7_Velostat mit nicht richitgem wiederstand.csv`, `atemkurve_10_Velostat richtig ausgelegt.csv`
  - Logs aus der Firmware: `logs/pocket-*.csv`, `logs/thermal-*.csv`
  - Velostat-Messreihe mit 481 Werten à 50 ms: identisch mit einer der atemkurve-Dateien?
- [ ] Fotos, CAD-Screenshots, Schaltplan in `abbildungen/`
- [x] Firmware-Repo gesichtet → `notizen/analyse_firmware.md`
- [ ] **Log-Dateien** `logs/pocket-*.csv` und `logs/thermal-*.csv` (per .gitignore nicht im Repo) → nach `daten/`
- [ ] Präsentation, Notizen in `notizen/`

## Formalia / Titelblatt
- [x] Titelblatt nach Vorlage Neffy 2
- [x] Labor: Labor für Kommunikation
- [x] Lehrkraft: Prof. Dr. Ilona Buchem
- [x] Betreuer: Prof. Dr. Manfred Hild
- [x] Abgabe: 26.10.2026
- [x] Ein gemeinsamer Teambericht; Kennzeichnung „wer was“ ganz am Ende
- [x] Teampartner: Younes Jamil
- [ ] Nachname Badre, beide Matrikelnummern
- [ ] „Praxisbericht“ oder „Praktikumsbericht“? (Neffy 2 nutzt „Praxisbericht“)
- [ ] Arbeitstitel bestätigen
- [ ] Wortlaut der Eigenständigkeitserklärung (BHT-Vorgabe)
- [ ] Umfang ~20 Seiten ohne Verzeichnisse/Anhang bestätigen

## Inhalt
- [x] Neffy 3.0 baut auf Neffy 2.0 auf (Raspberry Pi, Schulter- und Kopfbewegung)
- [x] Dynamixel → Schrittmotoren (mehr Kraft benötigt)
- [ ] Genaues Schrittmotor-Modell (Datenblatt)
- [ ] Probleme mit den Schrittmotoren (fürs Fazit) – und welches Team war zuständig?
- [x] Haptisches Feedback kam bei Neffy 1 und 2 gut an → Schulter-/Kopfbewegung übernommen
- [ ] Beleg dafür (Studie/Feedback), falls vorhanden
- [ ] Zeitraum und Stunden pro Person (für Kap. 2, Zeitaufteilung)
- [ ] Feingliederung bestätigen (aktuell = Gliederung aus CLAUDE.md)
- [ ] Anforderungen A1–A4: Entwurf abgleichen, prüfbare Kriterien ergänzen
- [ ] Aufgabenverteilung „Wer macht was“
- [x] Thermalsensor D6T-1A-02 integriert
- [ ] Datenblätter: D6T-1A-02, TMC2225, Schrittmotoren, Velostat
- [ ] Anforderung Anwesenheit: „nicht bei Vorbeigehen in 2–3 m“ (Notiz) vs. „reagiert kurz beim Vorbeigehen“ – was gilt?
- [x] Drucksensoren: FSR (Joy-IT) vs. Velostat, Gründe geklärt
- [x] Wurde der Dehnungsgurt (Backup) getestet? → nein, nur Idee (Kap. 4.2)
- [ ] Warum Wechsel von „Sensoren am Pi mit MCP3208“ zum ESP32-Board?
- [ ] Schaltung der Taschen: Spannungsteiler? Widerstandswert? Schaltplan
- [ ] Gehäuse-Infos (Badre schickt später)
- [x] Schnittstelle ESP32 ↔ Pi: UART 115200, Befehlssatz Neffy_UART_Interface
- [ ] A3/A4: Firmware sendet nur entspannt/normal/gestresst, keine Ein-/Ausatemdauer – Ziel anpassen?
- [ ] Quelle für Atemfrequenz in Ruhe (12–20/min), Grundlage der Einstufung
- [ ] Wer ist Younes Jamil / LegitimateShake (Teampartner? Team Programmierung?)
- [x] KI-Nutzung (Claude Code) bei Firmware und Bericht offenlegen → Kap. 4.4.7; Literatursuche nicht mehr als KI-Nutzung genannt (Entscheidung 21.10.2026)
- [ ] **Bei Prof. Buchem nachfragen, welche Form der KI-Angabe die BHT erwartet** → danach Kap. 4.4.7 und Eigenständigkeitserklärung anpassen
- [ ] Welche weiteren Messungen gibt es?
