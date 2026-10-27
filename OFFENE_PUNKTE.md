# Offene Punkte (Stand 27.10.2026, Abgabetag)

Ältere, erledigte Punkte stehen in der Git-Historie dieser Datei. Reviews: `notizen/review_2026-10-26.md`,
`notizen/review_ars_2026-10-26.md`, `notizen/gutachten_gremium_2026-10-27.md` (simuliertes Gremium).

## Vor der Abgabe heute
- [x] **Fotos** eingebaut (27.10.): Abb. 3.1c, 5.1a/b, 4.7 (lackierte Schulter, 4.3.4), 4.8 (Innenleben Körper
      und Kopf, 4.3.5). Zuschnitte in `abbildungen/fotos/` (einheitliche Formate), Originale in `abbildungen/`
- [ ] Kap. 3 (ca. 7 Zeilen) und Kap. 5 (ca. 5 Zeilen) ragen auf eine neue Seite – kürzen oder so lassen
- [x] Firmware-Teamanteil in 4.4.6 (Ideen/Funktionsumfang vom Team, Aufbau vom Werkzeug vorgeschlagen,
      iterativer Ablauf mit Tests am Board; 27.10., Younes). Achtung: 4.4.6 war „bleibt so“ (Eddy) – Eddy informieren
- [x] Begründungen in 4.3 (Teilung, PLA, Kleben statt Rundloch/Langloch, Magnete vs. Schrauben; 27.10.)
- [x] „geschätzte Einstufung des Stresslevels“ + „dazu passende Übung“ (2.1, Tab. 5.1, 6.1, 6.2; Younes 27.10.)
- [x] Stand der Technik ergänzt: Haynes 2022 (haptisches Atemkissen, 3.4), Zaccaro 2018 (langsames Atmen,
      3.2 und 4.4.4), Levinson 2014 (Tastendruck folgt Atemfrequenz, r = 0,99; 3.5) – alle geprüft
- [x] Mit Eddy abgesprochen (27.10.): 4.4.6 mit Teamanteil, drei neue Quellen
- [x] Neffy-2-Bericht gegengeprüft (liegt lokal als `daten/Praxisbericht.pdf`, per .gitignore ausgeschlossen):
      Kurbelschleife, zwei Displays nur für Augen, Riementrieb bis 25 mm, Zahnradantrieb Kopf, Sprachausgabe,
      XL430-W250, U2D2 + Power Hub, Magnete – alles bestätigt; Handlast 2–4 kg „ermittelt“ statt „geschätzt“
- [ ] **Abschluss:** Layout nach dem Einsetzen der Fotos (derzeit ragen Kap. 3 mit 10 und Kap. 5 mit 8 Zeilen auf eine
      neue Seite), `\usepackage[disable,…]{todonotes}`
      in `main.tex` (Platzhalter verschwinden damit NICHT), Endkontrolle, Pushen nur auf Eddys Ansage

## Entschieden (zur Erinnerung)
- KI-Angabe (4.4.7, Eigenständigkeitserklärung) bleibt so (Eddy, 26.10.)
- Keine weiteren Tests am Roboter; Validierung über die laufende Studie. Die Reichweitenmessung im Stehen ist
  auf sitzende Personen übertragbar (Oberkörper im Sichtfeld), im Betrieb vielfach sitzend erprobt (Younes, 27.10.)
- Roboter steht während der 30-s-Atemmessung still; Tests nur betreut, Kontaktflächen werden gereinigt (27.10.)
- 27 Ω: im Aufbau ermittelt; Erwärmung ausprobiert, unkritisch – im Bericht nicht weiter ausgeführt
- 4,7-kΩ-Kurve darf im Spannungsteiler-Diagramm bleiben (Rechenbeispiel, Younes 27.10.)
- Schrittmotoren und Lineareinheit: von Charly Görke ausgewählt, im Bericht genannt (2.3, 4.2.4, 5.5)
- Neffy-1-Bericht (Dincel & Thomas) nicht beschafft; Neffy 1.0 über `thomas2025neffy` belegt
- Seitenzahl ist kein hartes Limit (Vorgabe ca. 20 S., nicht streng); Ergänzungen sind möglich, wenn sie Punkte bringen
