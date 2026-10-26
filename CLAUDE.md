# Projekt: Praktikumsbericht – Neffy 3.0 (Team Sensorik)

## Kontext
- Studiengang: Bachelor Humanoide Robotik (HROB), BHT Berlin
- Hauptbetreuerin: Prof. Dr. Ilona Buchem (Titelblatt: „Lehrkraft“)
- Betreuer: Prof. Dr. Manfred Hild (Studiengangsleiter; Titelblatt: „Betreuer“)
- Durchgeführt im **Labor für Kommunikation** der BHT
- Gruppenprojekt: Team Sensorik und Team Programmierung; **kein eigenes Team Design** – eine Mitarbeiterin
  war für die grafische Gestaltung (z. B. Gesicht/Augen) zuständig. Abstimmung bei Bedarf in Online-Meetings
  mit gemeinsamer Abstimmung, dazu Umfragen zur Wahrnehmung der Gestaltung.
- Zielbild (Abb. 2.1) wurde von Prof. Buchem mit ChatGPT erzeugt.
- Display Neffy 3.0: Waveshare 4,3" DSI LCD, 800 × 480, kapazitiver Touch (`waveshare43dsi`).
- Antrieb: Dynamixel XL430-W250 (Neffy 2) zu schwach und laut → NEMA 17; Körper mit integrierter T8-Spindel
  (Hersteller vermutlich Iverntech, kürzere Spindel als 100 mm) → mehr Kraft, leiser. ESP32-Board ersetzt
  U2D2 + Power Hub (zu viel Platz); ESP32 erzeugt die Schrittimpulse.
- Kap. 2.2, 2.3 und 3.1 sind mit `\unsicher{}` grau markiert (Abstimmung Eddy/Younes) – nicht löschen.
- Unser Team: **Sensorik, 2 Personen** – **Eddy Werk** (GitHub eddy904) und Younes Jamil.
  Achtung: In früheren Notizen stand fälschlich „Badre“ – der Name ist Eddy Werk.
- Charly Goerke (GitHub „LegitimateShake“) ist Mitarbeiter im Labor für Kommunikation und Mitautor des
  Neffy-2-Berichts. Von ihm stammen der Entwurf des Neffy Boards und die UART-Bibliothek
  (Neffy_UART_Interface). Das ist **nicht** Eigenleistung des Teams und muss so gekennzeichnet werden.
- Die **Firmware im Repo ist maßgeblich**: Bei Widersprüchen zu Notizen gilt der Code.
- Bericht: **ein gemeinsamer Teambericht**. Wer was gemacht hat, wird erst ganz am Ende gekennzeichnet.
- Abgabeformat: LaTeX (VS Code + LaTeX Workshop), Literatur über biblatex (`literatur.bib`)
- Umfang: **ca. 20 Seiten** (laut Eddy nicht streng, 23.10.2026) von Einleitung bis Ende der Einschätzung; Titelblatt, Verzeichnisse,
  Literatur, Anhang und Eigenständigkeitserklärung zählen nicht mit [bitte bestätigen]
- Abgabe: **26.10.2026** (am 26.10. bestätigt; steht so auf dem Titelblatt)
- Sprache: Deutsch

## Referenzbericht
In `referenz/Praxisbericht.pdf` liegt der **Praxisbericht zu Neffy 2** (Goerke & Kazubski, BHT,
Labor für Kommunikation, 11.03.2025). Analyse: `notizen/analyse_praxisbericht_neffy2.md`.
**Die PDF ist per `.gitignore` vom (öffentlichen) Repo ausgeschlossen** und liegt nur lokal. Wer sie braucht,
bekommt sie direkt von Eddy. Alle für den Bericht wichtigen Fakten stehen in der Analyse-Notiz.
- **Verbindliche Vorlage für Titelblatt und Formalia** (Titelblatt-Layout, Kopfzeile, Abbildungen,
  Literaturstil). Die BHT-Grafik des Titelblatts liegt als `abbildungen/bht_titelseite.pdf` vor.
- **Ausgangspunkt und zitierbare Quelle** für Neffy 3.0 (`goerke2025neffy2` in `literatur.bib`).
  Inhalte nur mit Zitat verwenden, keine Formulierungen wörtlich übernehmen.
- Die Gliederung kommt **nicht** aus diesem Bericht, sondern aus der verbindlichen Gliederung unten.
- Der Neffy-2-Bericht deckt einige unserer Bewertungskriterien kaum ab: Es fehlen Anforderungen,
  Stand der Technik, Recherchemethodik, Messwerte, Evaluation, Fazit und Softwareablage.
  Unser Bericht muss hier mehr liefern.

## Bekannter Projektstand (aus früheren Notizen – mit mir abgleichen, nicht ungeprüft übernehmen)
- Neffy ist ein Tischroboter (Oberkörper ohne Arme, Bildschirm als Gesicht), der Atemübungen
  anleitet. Schultern und Kopf heben und senken sich im Atemrhythmus; die Nutzer:innen legen dabei die
  Hände auf die Schultern (haptischer Atemtakt).
- Neffy 3.0 baut direkt auf Neffy 2.0 auf (Bericht in `referenz/`), Neffy 2.0 auf Neffy 1.0
  (Bericht Dincel & Thomas, 2024 – noch nicht beschafft). Neffy 1.0 ist eine Weiterentwicklung von Ommie (Yale).
  - Übernommen: Raspberry Pi; Schulter- und Kopfbewegung nach dem Prinzip von Neffy 1.0/2.0, weil das
    haptische Feedback bei Neffy 1 und 2 sehr gut ankam. **Belegt:** `thomas2025neffy` (Neffy 1.0,
    Pilotstudie n = 25, STAI-6 signifikant gesenkt, Haptik als motivierend/natürlich beschrieben) und
    `buchem2026neffy2` (Neffy 2.0, n = 14 Geflüchtete, Roboter vs. Audio: subjektiv deutlich stärkere
    Stresssenkung, physiologische Werte uneinheitlich). Zu Neffy 3.0 gibt es noch keine Studie.
  - Atemgurte werden nur in Studien als Referenzmessung genutzt. Ein Gurt als Rückfallebene war bei uns
    nur eine Idee und wurde nicht getestet.
  - Geändert: Die Dynamixel-Motoren von Neffy 2.0 wurden durch **Schrittmotoren** ersetzt, weil mehr
    Kraft benötigt wurde (**NEMA 17**, Körper und Kopf; Körper: fertige Lineareinheit mit Spindel, Schlitten und Schiene,
    Kaufteile; das 3D-gedruckte Verbindungsteil Schlitten → Sensoreinsätze hat **das Team konstruiert**.
    Charly Goerke hat Motor und Schiene bereitgestellt und den Aufbau gezeigt – im Bericht nicht erwähnen).
    Problem: Bei sehr starkem Drücken bleibt der Körper stehen, Motor macht Geräusche (Ausblick: stärkerer Motor/Servo).
    Kopf: gedruckte Zahnräder haben Spiel (Ausblick: Metall oder Riemengetriebe).
- Ziele 3.0 (gesamt): sensorbasierte Interaktion, besserer Touch, Atemübungen per Interaktion auswählbar.
- Ursprünglicher Auftrag Team Sensorik:
  - Anwesenheitserkennung mit Thermalsensor Omron D6T-1A-02 (I²C) → Neffy „wacht auf“
  - Atemerkennung mit Velostat (Drucksensor, analog am ESP32) → Stresslevel einschätzen, Atemübung vorschlagen
- Elektronik: eigene Platine „Neffy Board“ / „Mainboard“ mit ESP32-S3, Kommunikation mit dem
  Raspberry Pi über UART (115200 Baud, Bibliothek Neffy_UART_Interface); WS2812B-LEDs (FastLED, PlatformIO).
  Firmware: https://github.com/YounesJamil/Neffy-3.0-Mainboard. Analyse: `notizen/analyse_firmware.md`
  (Hardware-Eckdaten, Erkennungsverfahren, Protokoll, Auffälligkeiten).
- Antrieb laut Firmware: Körper über Gewindespindel (8 mm Steigung, Verfahrweg in der Firmware auf max. 85 mm begrenzt; bei Übungen max. **20 mm** (Eddy); Ziel war mehr Kraft, nicht mehr Hub – Hub bleibt in der Größenordnung von Neffy 2 mit 25 mm), Kopf über Zahnräder
  30 → 40 Zähne (32°), TMC2225-Treiber, Referenzfahrt gegen Endschalter.
- Auswahl Drucksensor: getestet wurden FSR (verschiedene Größen) und Velostat. In den getesteten Aufbauten
  verhielt sich der FSR nahezu binär (sofort volle Spannung, keine abgestufte Kurve). Velostat war
  feinfühliger, besser einstellbar, lieferte abgestufte Kurven, erkannte schwächere Druckunterschiede, und
  Fläche und Form ließen sich frei wählen → Entscheidung für Velostat.
- Aufbau einer Tasche: 3D-gedruckter Grundkörper → Kupferfolie → Velostat → Kupferfolie, mit Silikon
  verschlossen; ein Rahmen dazwischen ermöglicht den Zusammenbau.
- Thermalsensor Omron D6T: recherchiert, gutes Preis-Leistungs-Verhältnis, anerkannter Hersteller; nur
  dieser eine wurde bestellt und erfüllte die Anforderungen. Kein Vergleichstest → ehrlich so darstellen,
  technische Einordnung (PIR/Kamera/ToF) über Kap. 3.
- Passive Atemerkennung: Hände ruhen in den Taschen, Atmung soll über leichte Gewichtsänderungen erkannt
  werden → nicht eindeutig genug. Messdaten existieren (folgen).
- Schaltplan existiert (folgt). Gehäuse-Infos folgen.
- Ergebnisse Atemerkennung:
  - Passive Erkennung (Hand auf der Schulter, Atembewegung) unzuverlässig – Signal zu verrauscht
  - Aktive Variante funktioniert: beim Einatmen drücken, beim Ausatmen loslassen → klare Flanken;
    nebenbei als Touch-Eingabe nutzbar
  - Umsetzung (Firmware): **30-s-Messung** auf Befehl, Atemfrequenz aus der mittleren Zeit zwischen
    Einatemzügen → Einstufung entspannt / normal / gestresst (Modul `BreathingDetection.cpp/.h`).
    An den Pi geht nur die Einstufung.
  - Empfehlung für die nächste Version: Velostat durch einfache Taster ersetzen
- Wendepunkt: Team Sensorik hat zusätzlich das komplette neue Gehäuse übernommen
  (SolidWorks-Konstruktion, FDM-3D-Druck, Nachbearbeitung, Lackierung) – größter Zeitanteil.
- Konstruktion: eiförmige Schale, gespiegelte Hälften, in druckbare Teile mit abnehmbarem Deckel geteilt;
  Rundloch-plus-Langloch war geplant, umgesetzt wurde fast überall **Kleben**; lösbar über Neodym-Magnete
  (Oberkörper, Kopfdeckel) bzw. Schrauben (hintere Klappe). 16 Druckteile (6 + 6 + 4), PLA (siehe Kap. 4.3).
- Herausforderungen: SolidWorks neu lernen, Druckbettgröße, lange Druckzeiten, Laborzeiten koordinieren,
  FDM-Toleranzen (angenommen 0,1 mm; **keine Testkörper** wegen begrenzter Druckkapazität, nur kleine Teile wie
  Aufnahmen für Netzteilbuchse, Schalter, Kopfhörer vorab getestet; Hülle nur einmal gedruckt) → eine Gehäuseversion.
- Atemkurven liegen in `daten/Messdaten_Atemsensorik/` (Übersicht + Kennwerte: `LIESMICH.txt`,
  `00_Uebersicht_Kennwerte.csv`): F1–F3 FSR SEN-Pressure10, P1–P2 Velostat mit nur aufgelegten Händen
  (passiv, bestätigt), A1–A6 Velostat mit aktivem Mitdrücken. Gemessen im April 2026 auf einem
  **ESP32-Entwicklungsboard** (nicht dem Neffy Board), Velostat mit 10-kΩ-Festwiderstand, 50 ms (F1: 200 ms).
  A3 (= Atemkurve 7) ist teils gesättigt, weil **zu fest gedrückt** wurde – nicht wegen eines falschen
  Widerstands (Notiz war falsch). Beim FSR wurden mehrere Festwiderstände (1 kΩ … 1 MΩ) probiert,
  der Einfluss war vernachlässigbar, das Verhalten blieb binär; im Bericht nur ein Satz dazu. Beim Velostat
  wirkt der Widerstand deutlich; begonnen mit 4,7 kΩ, endgültiger Wert offen (LIESMICH: 10 kΩ). Plots: `python daten/plots_atemsensorik.py` → `abbildungen/plots/`.
- Noch nicht im Ordner: Firmware-Logs `logs/pocket-*.csv` und `logs/thermal-*.csv`.
  Thermalsensor D6T-1A-02 ist final integriert.

## Arbeitsstand (26.10.2026)
| Kapitel | Stand | Fehlt noch |
|---|---|---|
| Titelblatt | fertig (Eddy Werk, Younes Jamil) | Matrikelnummern (erst lokal vor Abgabe), Abgabedatum prüfen |
| 1 Einleitung | fertig (26.10., 1 S.): Stress → Ommie/Neffy-Studien als einzige Quellen; Zielgruppe bewusst weit (Alltag, Kinder, belastete Gruppen), Projekt sucht noch den besten Einsatzfall; Kernbotschaft „vorgeben → reagieren“, sofort relativiert (geplant vollautomatisch, umgesetzt mit aktiver Mitwirkung) | – |
| 2 Ziel | 2.2 Anforderungen final (A7 ohne Maße); **2.3 Fragestellung gestrichen (26.10.)**; Tabelle „wer macht was“ in 2.3 Projektorganisation | Zeitraum/Stunden, Zeitaufteilung (optional) |
| 3 Stand der Technik | Fließtext, Vergleich Neffy 1/2/3; 3.1 grau `\unsicher` | Foto Neffy 3.0; Kamera-Punkt ohne Quelle (belegen oder streichen) |
| 4 Methoden | Fließtext inkl. **Theorie** (Spannungsteiler Gl./Abb., D6T-Sichtfeld + Reichweitenabschätzung 1,4–2 m, Spindelkraft-Gl.), CAD-Abb. 4.3; 4.1 Schnittstelle grau, UART-Tabelle per `\iffalse` raus | Haltemoment Motor + Wirkungsgrad η (Quelle) → Spindelkraft rechnen; Motorhersteller (Iverntech?); Nachname Kaspar; Festwiderstand final; Kleber; Druckermodelle bestätigen; Schaltplan |
| 5 Diskussion | Entwurf; Kennwerte als Diagramm (`daten/plot_kennwerte.py`), Tabelle in Anhang D; Evaluation A1–A10 | Fotos (frontal, Hände in Taschen); Anwesenheitsmessung 0,5–3 m mit `tools/thermal_log.py` (Firmware-Repo) → Plot + A1; **5.5 Eigene Ideen bestätigen**; wer führt die Studie durch |
| 6 Fazit | Entwurf (Younes, 23.10.) | ggf. auf 1 Seite verdichten |
| 7 Einschätzung | fertig (7.1–7.3 am 26.10.) | genauer Name des C++-Moduls |
Stand 26.10. abends: 4.1 nicht mehr grau (Ablauf mit Firmware-README geprüft), UART-Befehlstabelle in Anhang A, 5.5 Eigene Ideen geschrieben, 4.4.7 KI neu (Firmware-Code vollständig mit Claude Code, Ideen/Struktur vom Team; Bericht: LaTeX-Satz + Formulierungshilfe). Noch offen: Fotos, Festwiderstand (Farbcode rot-violett-schwarz-? unklar), Motor-Haltemoment/η, Thermalmessung (Younes), 3.1 grau, Zeitraum/Stunden.
| Anhang | Anhang D Kennwerte-Tabelle | Code-Auszüge, CAD-Zeichnungen, Schaltplan, Verweis Rohdaten |
| Erklärung | beide Unterschriftszeilen | Wortlaut der BHT |
Umfang: Kap. 1–7 ca. 29 S. (mit Markern); nicht streng. Kürzen Stufe 2 erledigt.

## Weiteres Vorgehen (für die nächste Sitzung, auch auf einem anderen PC)
1. **Kap. 1 Einleitung** im Interview schreiben (siehe Tabelle).
2. **Kap. 7.1–7.3** im Interview schreiben.
3. **Offene Fakten** bei Eddy einsammeln (`OFFENE_PUNKTE.md`), v. a. Haltemoment/Produktlink Motor,
   Taschenmaße, Nachname Kaspar, Festwiderstand, Zeitraum/Stunden.
4. **Entscheidungen Eddy/Younes:** grau markierte Abschnitte 2.2, 2.3, 3.1, 4.1 behalten/ändern/streichen;
   Messreihen A1–A6 → V1–V6 umbenennen (Verwechslung mit Anforderungen A1–A10)?; Schwachstelle
   `DISABLE_MOTORS` behalten?
5. **Material einbauen:** Fotos nach `abbildungen/fotos/` (`neffy3_frontal.jpg`, `haende_taschen.jpg`),
   Schaltplan als `abbildungen/schaltplan.pdf`, Thermal-Messung nach `daten/`.
6. **Beurteilungsbogen** (Tabelle unten) gezielt bedienen: Fotos für „Praktische Durchführung“ (30),
   Theorie ergänzen (20), 5.5 „Eigene Ideen“ (10), Mehrleistung als Sonderpunkte herausstellen (10).
7. **Abschluss:** Kennzeichnung „wer was“ (Eddy: SolidWorks/CAD/Gehäuse; Younes: ESP32-Firmware) als
   Tabelle in Kap. 2.4; KI-Angabe mit Prof. Buchem abstimmen; Marker entfernen
   (`\usepackage[disable,…]{todonotes}` in `main.tex`); Abbildungen/Leerseiten optimieren; ggf. weiter
   kürzen; Matrikelnummern lokal; Abgabedatum; Abschlussprüfung gegen Kriterien und Formalia.

## Technische Hinweise für Claude
- Build: `pdflatex main` → `biber main` → 2× `pdflatex main`. Plots/Tabellen neu erzeugen mit
  `python daten/plots_atemsensorik.py`, `daten/plot_kennwerte.py`, `daten/plot_spannungsteiler.py`,
  `daten/tabelle_kennwerte.py` (matplotlib mit pgf-Backend, pandas).
- **Bash-Heredocs verschlucken Backslashes** (`\\` → `\`, `\b` …): LaTeX-Ersetzungen nicht inline per
  Heredoc-Python machen, sondern Skript mit dem Write-Tool als Datei anlegen und dann ausführen – oder das
  Edit-Tool nutzen. Danach nach Zeilen mit einzelnem `\` am Ende suchen.
- Viele Dateien haben CRLF-Zeilenenden; Skripte sollten CRLF erhalten.
- Unsichere Abschnitte: Makro `\unsicher{…}` (gelber Kasten) + `{\color{gray} …}`.
- Randnotizen (`\todo`) nie in Tabellen/Abbildungen – dort `\todoi` (inline), sonst „Float(s) lost“.

Wichtige Einordnung (Kap. 3/4): Ommie bestimmt die Atemphase trotz Eigenbewegung des Roboters mit einem
eigenen Datensatz und einem neuronalen Netz (`matheus2023phase`). Unser Argument gegen den
Beschleunigungssensor deshalb so formulieren: möglich, aber mit großem Aufwand, bewusst der einfache Weg.

Literatur: Alle Einträge in `literatur.bib` sind geprüft (DOI über Crossref/OpenAlex, Datenblatt am Dokument).
Neue Quellen nur nach derselben Prüfung aufnehmen.

Gehäuse (Stand 22.10.): Oberkörper 6 Teile → 2 Hälften verklebt, in der Mitte magnetisch verbunden;
Unterkörper 6 Teile → Schale + hintere Klappe (6 Schrauben); Kopfhülle 4 Teile (Deckel magnetisch,
Hinterteil verschraubt, Vorderteil zwei Stifte). **Rundloch-Langloch wurde verworfen – fast alles geklebt.**
Drucker Prusa MK4S und i3 MK3S, große Teile je ≥ 15 h, Toleranzannahme 0,1 mm, oft nachgebohrt.
Kopfmechanik: Caspar Jaki (Team Programmierung). Pi sitzt im Kopf. Schwachstelle: Hände/Ellbogen etwas zu
hoch → Kissen (Kap. 5/6). Druckerverfügbarkeit eingeschränkt → neutral in Kap. 7.
Material PLA. Nachbearbeitung: Klebekanten mit Sekundenkleber gefüllt, von Hand geschliffen (Elektroschleifer
beschädigt PLA), Spachteln wäre an manchen Stellen besser gewesen. Lack: Kunststoffprimer → Haftgrund
(Vincent, Hellweg) → 2–3 Schichten Montana GOLD „Sahara Beige“; lange Trockenzeiten. Ausblick: Teile möglichst
am Stück drucken und Stützmaterial in Kauf nehmen, spart Nacharbeit.

## Öffentliches Repo – Datenschutz
Das GitHub-Repo ist **öffentlich**. Keine Matrikelnummern oder andere persönliche Daten committen; diese
erst kurz vor der Abgabe lokal eintragen. Fremde Berichte (z. B. `referenz/`) bleiben per `.gitignore` draußen.

## Material
Das Projektmaterial wird nach und nach in diesen Ordner hochgeladen (`daten/`, `abbildungen/`, `notizen/`,
Code bzw. Repo-Link, Präsentation). Bei neuem Material: sichten, kurz zusammenfassen, dem passenden
Kapitel zuordnen, „Bekannter Projektstand“ ggf. korrigieren und offene Punkte in `OFFENE_PUNKTE.md` abhaken.

## Deine Rolle
Du unterstützt beim Schreiben eines wissenschaftlichen Praktikumsberichts.
Du strukturierst, formulierst, prüfst und setzt in LaTeX um. Die Inhalte (was gemacht wurde,
Messwerte, Entscheidungen) kommen von mir bzw. aus dem Material in diesem Ordner.

## Arbeitsweise beim Schreiben (vereinbart am 21.10.2026)
Kapitel für Kapitel, im Interview:
1. Claude fragt gezielt, was in das Kapitel bzw. den Abschnitt gehört (konkrete Fragen, Bekanntes vorausgefüllt).
2. Eddy beschreibt den Inhalt in Stichpunkten oder frei formuliert.
3. Claude formuliert daraus den Fließtext in LaTeX, kompiliert und meldet zurück:
   - wo eine Literaturrecherche sinnvoll ist (und was gesucht wird),
   - welche Messdaten/Auswertungen, Bilder/Fotos oder Angaben aus dem Neffy-1/2-Bericht noch fehlen,
   - Anregungen, was im Kapitel noch fehlt oder besser belegt werden sollte.
Die Kennzeichnung „wer hat was gemacht“ erfolgt erst am Ende.

**Git:** Nach Änderungen nur **lokal committen**. **Gepusht wird erst, wenn Eddy es ausdrücklich sagt**
(Wunsch vom 22.10.2026).

## KI-Nutzung
Als KI-Werkzeug wurde ausschließlich **Claude Code** verwendet. Das wird in Kap. 4.4.7
(„Einsatz von KI-Werkzeugen“) offengelegt: Gliederung, Formulieren, LaTeX-Satz, Analyse der Firmware
und Entwicklung der Firmware. **Die Literatursuche wird nicht als KI-Nutzung aufgeführt**, und Kap. 3.1
(Recherchemethodik) nennt nur Datenbanken, Suchbegriffe und Auswahlkriterien (Entscheidung Eddy,
21.10.2026). Der Satz „Inhalte, Messwerte und Entscheidungen stammen vom Team; alle Quellen über DOI bzw.
Originaldokument geprüft“ bleibt. Offen: bei Prof. Buchem klären, welche Form der KI-Angabe die BHT
erwartet; danach Kap. 4.4.7 und Eigenständigkeitserklärung anpassen.

## Harte Regeln
- Erfinde NIEMALS Messwerte, Ergebnisse, Quellen, Zitate oder Seitenzahlen.
- Fehlt etwas, setze einen sichtbaren Marker `\todo{Was fehlt}` (Paket `todonotes`) und sammle
  offene Punkte in `OFFENE_PUNKTE.md`.
- Literatur nur aufnehmen, wenn sie real und überprüfbar ist (DOI, Verlag, URL). Unsichere Quellen markieren statt raten.
- Trenne klar: Gesamtprojekt (alle Teams) – Team Sensorik – individueller Anteil.
- Die anderen Teams nur so weit beschreiben, wie es für unsere Schnittstellen nötig ist.
- Frag nach, bevor du größere Umstrukturierungen machst.

## Verbindliche Gliederung
Seitenzahlen = Richtwerte für ~20 Seiten.

**Titelblatt** (wie Praxisbericht Neffy 2): BHT-Grafik rechts, Titel, „Labor für Kommunikation“,
„Team Sensorik“, vorgelegt von (Name + Matr.-Nr.), Lehrkraft, Betreuer, Studiengang, Abgabedatum.
Zeitraum und Dauer (Stunden) gehören in Kap. 2 (Projektorganisation), nicht aufs Titelblatt.
**Inhaltsverzeichnis**

1. **Einleitung** (~1 S.) – Hinführung: Stress, Atemübungen, soziale Roboter; worum es im Bericht geht
2. **Ziel der Arbeit** (~2 S.)
   - Zielstellung (Neffy 2.0 → 3.0, Auftrag Team Sensorik, später Gehäuse)
   - Anforderungsdefinition – nummerierte Tabelle, funktional/nicht-funktional, prüfbar (A1, A2, …)
   - Übergeordnete Fragestellung (als hervorgehobene Frage)
   - Projektorganisation und Aufgabenverteilung – **Pflichttabelle „Wer macht was“** im Team Sensorik
     + Schnittstellen zu Programmierung und Design; Zeitraum, Stunden und Zeitaufteilung pro Person
     (wie im Neffy-2-Bericht als Diagramm)
3. **Stand der Technik und Wissenschaft** (~2–3 S.)
   - **Vorgabe der Betreuerin:** Studien zu Ommie, Neffy 1.0 und Neffy 2.0 aufnehmen und Neffy 3.0 als
     „Stand der Technik“ mit 2.0 und 1.0 vergleichen. Studien zu Neffy siehe ORCID
     https://orcid.org/0000-0002-9189-7217 (bereits eingetragen: `thomas2025neffy`, `buchem2026neffy2`).
   - kurz: Recherchemethodik (Datenbanken, Suchbegriffe, Auswahlkriterien)
   - Ansätze in Kategorien einordnen, je mit Beispielen + Abbildung, dann Vor-/Nachteile vergleichen
     (z. B. Atemerkennung: kontaktbasiert / berührungslos; Anwesenheitserkennung: PIR, Thermopile, Kamera, ToF;
     Roboter/Geräte für Atemübungen)
   - Abschluss: Einordnung von Neffy 3.0 in diese Landschaft
4. **Verfahren und Methoden** (~6–7 S.)
   - Systemarchitektur (Blockdiagramm: Sensoren → Neffy Board/ESP32-S3 ↔ Raspberry Pi ↔ Motor/Display)
   - Hardware / Sensorik: Lösungsauswahl mit Begründung (Bewertungsmatrix), v. a. Vergleich der
     getesteten Drucksensoren → Entscheidung für Velostat; Messaufbau, Schaltung
   - Konstruktion Gehäuse: Iterationen mit Abbildungen (CAD → Teilung → Druck → Nachbearbeitung),
     Entscheidungen begründen (Teilung, Kleben statt Passstifte, Magnete/Modularität, Toleranzen)
   - Software: Signalverarbeitung/Atemerkennung, Struktur, Softwareablage (Repo, Build), KI-Nutzung transparent nennen
5. **Diskussion der Ergebnisse** (~3–4 S.)
   - Funktionsnachweis (Fotos des fertigen Neffy)
   - Messwerte: Tabellen + Diagramme, Auswertung
   - Evaluation gegen die Anforderungen A1, A2, … (Tabelle: erfüllt / teilweise / nicht erfüllt)
   - Schwachstellen ehrlich und konkret (Zahlen, Ursachen), auch was nicht funktioniert hat
6. **Fazit** (~1 S.)
   - Zusammenfassung
   - Ausblick (konkret: z. B. Taster statt Velostat, nächste Gehäuseversion, Antrieb)
7. **Meine/Unsere Einschätzung zum Praktikum** (~2–3 S.) – Ich-/Wir-Form erlaubt
   - Studium und Praktikum · Praktikumsalltag · Erwartungen · Erfahrungen
     (hier Selbstständigkeit, Motivation, Teamarbeit mit konkreten Beispielen) · Persönliches Fazit

**Abbildungsverzeichnis · Abkürzungsverzeichnis · Literaturverzeichnis · Anhang** (Code-Auszüge, CAD-Zeichnungen,
Rohdaten, Schaltplan) · **Eigenständigkeitserklärung** (Ort, Datum, Name)

## Bewertungskriterien (Beurteilungsbogen Praxisphase, FB VII – `notizen/Beurteilbogen_Praxisphase.pdf`)
| Nr. | Kriterium (Bogen) | Punkte | Kapitel |
|---|---|---|---|
| 1 | Umfang und Schwierigkeitsgrad der gestellten Aufgabe | 0–5 | 2 (Aufgabe, Erweiterung) |
| 2 | Ermittlung des Standes der Technik / Literaturrecherche | 0–10 | 3 |
| 3 | Theoretischer Ansatz | 0–20 | 3 / 4 (Gleichungen, Abschätzungen) |
| 4 | Anteil eigener Ideen | 0–10 | 5.5 (explizit benennen), 4 |
| 5 | Praktische Durchführung / Funktionsfähigkeit | 0–30 | 4 + 5.1 (Fotos!) |
| 6 | Auswertung / Analyse der Ergebnisse | 0–10 | 5 |
| 7 | Arbeitsstil, Motivation, Selbstständigkeit, Zusammenarbeit im Team | 0–15 | 2.4 + 7 |
| 8 | Sonderpunkte | 0–10 | Mehrleistung (Gehäuse, Modularität) herausstellen |
Summe 110 (inkl. 10 Sonderpunkte); Notenstufen laut Bogen: 96–100 → 1,0; 90–95 → 1,3; 81–89 → 1,7;
74–80 → 2,0; 67–73 → 2,3; 57–66 → 2,7; 50–56 → 3,0; … < 20 → 5,0. Der Bogen hat außerdem Felder „Aufgabenstellung“
und „Durchgeführte Aufgaben“ → in Kap. 2 klar trennbar machen.

## Stil und Formalia
- Layout wie Praxisbericht Neffy 2: Kopfzeile links Kapitel, rechts „Praktikumsbericht Neffy 3.0“,
  Seitenzahl unten mittig, Serifenschrift auch in Überschriften.
- Fachkapitel sachlich und überwiegend unpersönlich (Passiv/„es wurde …“); Ich-/Wir-Form nur in Kap. 7
  und sparsam am Anfang der Diskussion.
- Jede Abbildung nummeriert, beschriftet und im Text referenziert („siehe Abbildung 3“);
  Unterabbildungen (a), (b), (c) mit `subcaption`; fremde Bilder mit Quellenangabe in der Bildunterschrift.
- Entscheidungen im Muster: Problem → Optionen → Kriterien → Entscheidung → Begründung
  (genau das fehlt im Neffy-2-Bericht, z. B. bei Spindel- vs. Riementrieb).
- Iterationen sichtbar machen (Versionen mit Abbildungen nebeneinander, auch Neffy 2 vs. Neffy 3.0).
- Rechnungen mit Datenblattwerten und nummerierten Gleichungen (Vorbild: Drehmoment-Rechnung und
  Strombudget im Neffy-2-Bericht).
- Diskussion mit konkreten Zahlen und Ursachen statt allgemeiner Aussagen; Datenblätter zitieren.
- Auch Gescheitertes (passive Atemerkennung) sauber als Ergebnis darstellen.
- Abkürzungen beim ersten Auftreten ausschreiben, Abkürzungsverzeichnis per `acro` oder `glossaries`.
- Literatur: biblatex, numerisch [1], mit DOI/URL und „besucht am“; bevorzugt Fachliteratur
  (ACM, IEEE, Frontiers, Sensors/MDPI) + Datenblätter + Vorgängerberichte zu Neffy 1.0 und 2.0.

## Vorgehen – in dieser Reihenfolge
1. **Bestandsaufnahme:** Lies alles im Ordner (Notizen, Code, Messdaten, Bilder, Präsentation, Referenzbericht).
   Fasse zusammen, was vorhanden ist, und gleiche es mit „Bekannter Projektstand“ ab.
2. **Lückenanalyse:** Tabelle `Kriterium → vorhandenes Material → fehlt noch`. Dann gezielte Fragen.
3. **Feingliederung:** Unterkapitel innerhalb der verbindlichen Gliederung festlegen. Warte auf mein OK.
4. **LaTeX-Gerüst:** `main.tex`, Titelblatt, ein Kapitel pro Datei in `kapitel/`, `abbildungen/`, `daten/`,
   `literatur.bib`, `anhang/`. Muss fehlerfrei kompilieren.
5. **Kapitelweise schreiben:** nach jedem Kapitel kompilieren, Fehler beheben, Seitenzahl prüfen.
6. **Messdaten:** Tabellen und Diagramme direkt aus den Dateien in `daten/` erzeugen
   (pgfplots oder Python → PDF), nicht abtippen.
7. **Abschlussprüfung:** Kriterientabelle + Aufgabenverteilungstabelle + Formalia einzeln durchgehen und zeigen,
   wo alles erfüllt ist und wo es noch schwach ist.
Anforderungen ab 26.10.: A1–A8 (Zielbild = nur Inspiration, kein A mehr; FDM-Druckbarkeit gestrichen; alt A7→A6 Hände (erfüllt), A8→A7 Zugang, A10→A8 Bedienung). Tabellen: booktabs + graue Trennlinien \trenn (main.tex).
