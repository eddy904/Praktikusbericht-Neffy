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
    Charly Goerke hat Schrittmotoren und Lineareinheit ausgewählt und bereitgestellt – wird seit 26.10.
    im Bericht genannt: 2.3, 4.2.4, 5.5; Entscheidung Eddy).
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
  wirkt der Widerstand deutlich; Messreihen mit 10 kΩ; im fertigen Roboter neu gebaute, größere Sensoreinsätze (gleicher
  Aufbau) mit 27 Ω, im Aufbau ermittelt, feinere Auflösung; keine eigenen Messreihen dazu nötig.
  4,7 kΩ im Bericht nicht erwähnen (Eddy, 26.10.). Plots: `python daten/plots_atemsensorik.py` → `abbildungen/plots/`.
- Noch nicht im Ordner: Firmware-Logs `logs/pocket-*.csv` und `logs/thermal-*.csv`.
  Thermalsensor D6T-1A-02 ist final integriert.

## Arbeitsstand (26.10.2026, abends)
| Teil | Stand | Offen |
|---|---|---|
| Titelblatt | fertig; Matrikelnummern kommen aus der lokalen `matrikelnummern.tex` (per `.gitignore` ausgeschlossen, Makros `\matrEddy`, `\matrYounes`) | – |
| 1 Einleitung | fertig (1 S.): Stress → Ommie/Neffy-Studien; Zielgruppe bewusst weit; „vorgeben → reagieren“, sofort relativiert (aktive Mitwirkung nötig) | – |
| 2 Ziel | fertig. Zielbild = nur Inspiration (Brainstorming), keine Anforderung. Anforderungen **A1–A8** (alt A6 Zielbild und A9 Druckbarkeit gestrichen → A6 Hände, A7 Zugang, A8 Bedienung). Fragestellung gestrichen. Projektorganisation: März–Ende Okt. 2026, geschätzt 450 h/Person, Tabelle „Wer macht was“, Kreisdiagramm Zeitaufteilung (geschätzt: Konstruktion 35, Druck/Nachbearbeitung 25, Programmierung 20, Sensortests 8, Montage/Löten 7, Abstimmung/Beschaffung/Doku 5 %) | – |
| 3 Stand der Technik | fertig; 3.1 ohne Hinweis auf nachträgliche Recherche | Foto Neffy 3.0 (Abb. 3.1c) |
| 4 Methoden | fertig: Kommunikation mit Firmware-README geprüft; Handmaße-Tabelle (`maldonado2023exhand` Tab. 1, `fu2022tfcc` Tab. 3); Festwiderstand 27 Ω (bestätigt); Motor 42HB4027-41 (kein Datenblatt gefunden); Spindel-Abschätzung Gl. 4.6–4.9 (η aus Geometrie, μ = 0,1–0,2 angenommen, nicht selbsthemmend); Kopfmechanik Caspar Jaki; Druck in der HROB-Werkstatt; KI-Angabe 4.4.7 final (Firmware-Code vollständig mit Claude Code, Ideen/Struktur vom Team) | optional Foto lackiertes Gehäuse |
| 5 Diskussion | fertig: Evaluation A1–A8 + A3* (A3 passiv nicht erfüllt, A3* aktiv erfüllt, A1 vorläufig); Antriebs-Stillstand: Heben = Motormoment überschritten, von oben = fehlende Selbsthemmung; 5.5 Eigene Ideen mit Namen (Konzept Team, Code Claude Code); Messreihen = Sensorauswahl am Entwicklungsboard, 2 Personen (Team); Studie durch Mitarbeiterin der grafischen Gestaltung | Fotos Abb. 5.1; Thermal-Reichweitenmessung inkl. ruhiges Sitzen > 20 s (Younes, wird nachgereicht) |
| 6 Fazit | fertig | – |
| 7 Einschätzung | fertig | – |
| Anhang | A: UART-Befehle + `BreathingDetection.h/.cpp` (Kopie in `anhang/code/`, Commit 2693747); B: Kennwerte + Verweis Rohdaten. CAD- und Schaltplan-Anhang gestrichen (kein Material) | – |
| Erklärung | übliche Formel in Wir-Form inkl. KI-Hinweis (kein BHT-Wortlaut gefunden) | – |

Umfang: Kap. 1–7 = 37 S., PDF 52 S.; nicht streng (Eddy).
**Review 26.10. erledigt** (`notizen/review_2026-10-26.md`, alle Textpunkte umgesetzt): A3* in Tab. 2.1 und 5.1
(„im Projektverlauf ergänzt“), A1 vorläufig, Antrieb, Beschleunigungssensor an Ommie angeglichen, Tab. 3.1
Anwesenheitssensoren, Klassengrenzen 5,5/10,5, „Atemtakt angeben“ in Einleitung/Fazit, 27 Ω (neue, größere
Sensoreinsätze, im Aufbau ermittelt), Velostat-Einbau schrittweise abgestimmt, Taschen im Mittel 20 × 16 × 6 cm,
Druckbereich 14 × 8 cm (leichte Klicks mittig am zuverlässigsten), Kap. 7 „Rückblickend …“.
Keine weiteren Tests am Roboter – Validierung über die laufende Studie (Entscheidung Eddy).
Layout: booktabs + graue Trennlinien `\trenn` (main.tex); Gleitobjektseiten beginnen oben; alle Abbildungen und
Tabellen am 26.10. auf Ausrichtung geprüft.

## Weiteres Vorgehen (für die nächste Sitzung, auch auf einem anderen PC)
1. ~~Review~~ – erledigt am 26.10. (siehe oben).
2. **Fotos** nach `abbildungen/fotos/` (`neffy3_frontal.jpg`, `haende_taschen.jpg`) und Platzhalter in
   Abb. 3.1c und 5.1a/b ersetzen. `\platzhalter` verschwindet NICHT mit `[disable]`. Optional Foto des
   lackierten Gehäuses (`\todo` in 4.3.4).
3. **Thermalmessung** (0,5–3 m, `tools/thermal_log.py` im Firmware-Repo) → Plot + Zahl für A1 in 5.2.6;
   dabei prüfen, ob eine ruhig sitzende Person > 20 s erkannt bleibt. Danach A1 in Tab. 5.1 von
   „vorläufig“ auf erfüllt/teilweise setzen. Sonst Satz „nur beobachtet, nicht systematisch gemessen“ + Ausblick.
3a. **Thermalsensor-Firmware wird noch geändert (Eddy, 26.10.):** Auf Eddys Bescheid das Firmware-Repo
   neu lesen und 4.2.1, 4.4.2, 5.2.6 und Tab. 5.1 (A1/A2) abgleichen. Sitzen vs. Vorbeigehen wird
   indirekt über die Dauer der Meldung unterschieden (kurz hoch- und runterfahren beim Vorbeigehen).
4. **Abschluss:** `\usepackage[disable,…]{todonotes}` in `main.tex`; Endkontrolle; pushen nur auf Eddys Ansage.

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
Originaldokument geprüft“ bleibt. Kap. 4.4.7 und Eigenständigkeitserklärung bleiben so (Eddy, 26.10.).

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
