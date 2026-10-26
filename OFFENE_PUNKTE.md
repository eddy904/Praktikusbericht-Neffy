# Offene Punkte (Stand 26.10.2026, abends)

Ältere, erledigte Punkte stehen in der Git-Historie dieser Datei. Reviews: `notizen/review_2026-10-26.md`,
`notizen/review_ars_2026-10-26.md`.

## Wartet auf das Team
- [ ] **Thermalsensor-Fix pushen** (Vergleich mit der eigenen Sensortemperatur statt gelernter
      Raumtemperatur) → danach Firmware-Repo neu lesen und anpassen: 4.2.1, 4.4.2 inkl. Gl. 4.10
      (Satz zum Zielkonflikt wieder streichen), 5.2.6 (Absatz Sonne/Heizkörper), Tab. 5.1 A1.
      Offen: Gibt es das Neulernen nach 20 s noch? Erwärmt sich der Sensor im Gehäuse selbst?
- [ ] **Reichweitenmessung Thermalsensor** (Younes, 0,5–3 m, `tools/thermal_log.py`) → Zahl/Plot in
      5.2.6, A1 in Tab. 5.1 von „vorläufig“ auf erfüllt/teilweise
- [ ] **Fotos** nach `abbildungen/fotos/`: Neffy frontal (Abb. 3.1c, 5.1a), Hände in den Taschen (Abb. 5.1b),
      optional lackiertes Gehäuse (`\todo` in 4.3.4)
- [ ] **Kürzen:** Vorschläge liegen vor (Chat 26.10.), Entscheidung Eddy

## Kann Claude direkt erledigen (nach Freigabe)
- [ ] A6 in Tab. 5.1: Ergonomie (Ellbogen zu hoch) im Status abbilden; Anzahl/Spannweite der Probehände,
      falls bekannt

## Abschluss
- [ ] Matrikelnummern lokal in `matrikelnummern.tex` (nicht committen)
- [ ] `\usepackage[disable,…]{todonotes}` in `main.tex`; Platzhalter verschwinden damit NICHT
- [ ] Endkontrolle (Verweise, Abbildungen, Seitenumbrüche)
- [ ] Pushen – nur auf Eddys Ansage

## Entschieden (zur Erinnerung)
- KI-Angabe (4.4.7, Eigenständigkeitserklärung) bleibt so (Eddy, 26.10.)
- Keine weiteren Tests am Roboter; Validierung über die laufende Studie
- 27 Ω: im Aufbau ermittelt; Erwärmung ausprobiert, unkritisch – im Bericht nicht weiter ausgeführt
- Stand der Technik wird nicht erweitert (Länge); höchstens ersetzen
- Schrittmotoren und Lineareinheit: von Charly Goerke ausgewählt, im Bericht genannt (2.3, 4.2.4, 5.5)
- Neffy-1-Bericht (Dincel & Thomas) nicht beschafft; Neffy 1.0 über `thomas2025neffy` belegt
