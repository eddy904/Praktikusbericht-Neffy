# Projekt: Praktikumsbericht – Neffy 3.0 (Team Sensorik)

## Kontext
- Studiengang: Bachelor Humanoide Robotik (HROB), BHT Berlin
- Betreuung: Prof. Dr. Ilona Buchem
- Gruppenprojekt mit drei Teams: Sensorik, Programmierung, Design
- Unser Team: **Sensorik, 2 Personen** – Badre und [Name Teampartner:in]
- Bericht: [gemeinsamer Teambericht ODER Einzelbericht pro Person – bitte festlegen]
- Abgabeformat: LaTeX (VS Code + LaTeX Workshop), Literatur über biblatex (`literatur.bib`)
- Umfang: **ca. 20 Seiten** von Einleitung bis Ende der Einschätzung; Titelblatt, Verzeichnisse,
  Literatur, Anhang und Eigenständigkeitserklärung zählen nicht mit [bitte bestätigen]
- Abgabe: **31.10.2026**
- Sprache: Deutsch

## Referenzbericht
In `referenz/` liegt der Praktikumsbericht eines Kommilitonen (anderes Projekt: „Headset-Lift“).
- Nur als Vorlage für **Gliederung, Aufbau, Tonfall und Formalia** verwenden.
- Keine Inhalte, Formulierungen oder Quellen daraus übernehmen.
- Die Hauptkapitel sind verbindlich (außer „Praktikumsstelle“, die entfällt). Die Unterkapitel dort
  sind projektspezifisch – unsere werden auf Neffy zugeschnitten.
- Der Referenzbericht deckt einige unserer Bewertungskriterien kaum ab (keine explizite
  Anforderungsliste, keine Messwerte/Tabellen, keine Recherchemethodik, keine Softwareablage).
  Unser Bericht muss hier mehr liefern.

## Bekannter Projektstand (aus früheren Notizen – mit mir abgleichen, nicht ungeprüft übernehmen)
- Neffy ist ein Tischroboter (Oberkörper ohne Arme, Bildschirm als Gesicht), der Atemübungen
  anleitet. Ein Motor-Mechanismus bewegt den Roboter hoch und runter und visualisiert so den Atemrhythmus.
  Neffy 3.0 baut auf Neffy 2.0 auf (Vorgängerversion = Ausgangspunkt, wie V3 im Referenzbericht).
- Ziele 3.0 (gesamt): sensorbasierte Interaktion, besserer Touch, Atemübungen per Interaktion auswählbar.
- Ursprünglicher Auftrag Team Sensorik:
  - Anwesenheitserkennung mit Thermalsensor Omron D6T-1A-02 (I²C) → Neffy „wacht auf“
  - Atemerkennung mit Velostat (Drucksensor, analog am ESP32) → Stresslevel einschätzen, Atemübung vorschlagen
- Elektronik: eigene Platine „Neffy Board“ mit ESP32-S3, Kommunikation mit Raspberry Pi;
  WS2812B-LEDs (FastLED, PlatformIO) funktionieren.
- Auswahl Drucksensor: Es wurden mehrere Drucksensor-Ansätze getestet (u. a. FSR [weitere bitte ergänzen]).
  Sehr schnell zeigte sich, dass Velostat am besten geeignet ist. → Zentrales Beispiel für
  „begründete Auswahl von Lösungsansätzen“: getestete Varianten, Kriterien, Beobachtungen, Entscheidung
  (Bewertungstabelle). Gründe für Velostat bei mir erfragen, nicht erfinden.
- Ergebnisse Atemerkennung:
  - Passive Erkennung (Hand auf der Schulter, Atembewegung) unzuverlässig – Signal zu verrauscht
  - Aktive Variante funktioniert: beim Einatmen drücken, beim Ausatmen loslassen → klare Flanken;
    nebenbei als Touch-Eingabe nutzbar
  - Auswertungsidee: 20-s-Fenster, mittlerer Atemrhythmus; Modul als eigene `.cpp`/`.h`
  - Empfehlung für die nächste Version: Velostat durch einfache Taster ersetzen
- Wendepunkt: Team Sensorik hat zusätzlich das komplette neue Gehäuse übernommen
  (SolidWorks-Konstruktion, FDM-3D-Druck, Nachbearbeitung, Lackierung) – größter Zeitanteil.
- Konstruktion: eiförmige Schale, gespiegelte Hälften, in druckbare Teile mit abnehmbarem Deckel geteilt;
  Ausrichtung über Passstifte Ø5/Ø6 mm mit Rundloch-plus-Langloch-Prinzip.
- Herausforderungen: SolidWorks neu lernen, Druckbettgröße, lange Druckzeiten, Laborzeiten koordinieren,
  FDM-Toleranzen (empirisch über Testkörper ermittelt statt ISO-Passungen) → bisher nur eine Gehäuseversion.
- Bekannte Messreihe: Velostat-Spannungsverlauf, 481 Werte im 50-ms-Takt (~24 s). Weitere Messdaten in `daten/`.
- Offen/zu klären: Wurde der Thermalsensor final integriert? Welche Messungen gibt es noch?

## Material
Das Projektmaterial wird nach und nach in diesen Ordner hochgeladen (`daten/`, `abbildungen/`, `notizen/`,
Code bzw. Repo-Link, Präsentation). Bei neuem Material: sichten, kurz zusammenfassen, dem passenden
Kapitel zuordnen, „Bekannter Projektstand“ ggf. korrigieren und offene Punkte in `OFFENE_PUNKTE.md` abhaken.

## Deine Rolle
Du unterstützt beim Schreiben eines wissenschaftlichen Praktikumsberichts.
Du strukturierst, formulierst, prüfst und setzt in LaTeX um. Die Inhalte (was gemacht wurde,
Messwerte, Entscheidungen) kommen von mir bzw. aus dem Material in diesem Ordner.

## Harte Regeln
- Erfinde NIEMALS Messwerte, Ergebnisse, Quellen, Zitate oder Seitenzahlen.
- Fehlt etwas, setze einen sichtbaren Marker `\todo{Was fehlt}` (Paket `todonotes`) und sammle
  offene Punkte in `OFFENE_PUNKTE.md`.
- Literatur nur aufnehmen, wenn sie real und überprüfbar ist (DOI, Verlag, URL). Unsichere Quellen markieren statt raten.
- Trenne klar: Gesamtprojekt (alle Teams) – Team Sensorik – individueller Anteil.
- Die anderen Teams nur so weit beschreiben, wie es für unsere Schnittstellen nötig ist.
- Frag nach, bevor du größere Umstrukturierungen machst.

## Verbindliche Gliederung (Hauptkapitel aus dem Referenzbericht, Unterkapitel für Neffy)
Seitenzahlen = Richtwerte für ~20 Seiten.

**Titelblatt** (BHT-Stil): „Praktikumsbericht“, durchgeführt im: [Labor/Fachgebiet], vorgelegt von,
Matr.-Nr., Betreuerin, Zeitraum, Dauer (Wochen/Stunden), Fachbereich, Studiengang, Abgabedatum, BHT-Logo
**Inhaltsverzeichnis**

1. **Einleitung** (~1 S.) – Hinführung: Stress, Atemübungen, soziale Roboter; worum es im Bericht geht
2. **Ziel der Arbeit** (~2 S.)
   - Zielstellung (Neffy 2.0 → 3.0, Auftrag Team Sensorik, später Gehäuse)
   - Anforderungsdefinition – nummerierte Tabelle, funktional/nicht-funktional, prüfbar (A1, A2, …)
   - Übergeordnete Fragestellung (als hervorgehobene Frage, wie im Referenzbericht)
   - Projektorganisation und Aufgabenverteilung – **Pflichttabelle „Wer macht was“** im Team Sensorik
     + Schnittstellen zu Programmierung und Design
3. **Stand der Technik und Wissenschaft** (~2–3 S.)
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
     Entscheidungen begründen (Teilung, Passstifte, Toleranz-Testkörper)
   - Software: Signalverarbeitung/Atemerkennung, Struktur, Softwareablage (Repo, Build), KI-Nutzung transparent nennen
5. **Diskussion der Ergebnisse** (~3–4 S.)
   - Funktionsnachweis (Fotos des fertigen Neffy)
   - Messwerte: Tabellen + Diagramme, Auswertung
   - Evaluation gegen die Anforderungen A1, A2, … (Tabelle: erfüllt / teilweise / nicht erfüllt)
   - Schwachstellen ehrlich und konkret (Zahlen, Ursachen), auch was nicht funktioniert hat
6. **Fazit** (~1 S.)
   - Zusammenfassung
   - Ausblick (konkret: z. B. Taster statt Velostat, nächste Gehäuseversion, Materialwahl)
7. **Meine/Unsere Einschätzung zum Praktikum** (~2–3 S.) – Ich-/Wir-Form erlaubt
   - Studium und Praktikum · Praktikumsalltag · Erwartungen · Erfahrungen
     (hier Selbstständigkeit, Motivation, Teamarbeit mit konkreten Beispielen) · Persönliches Fazit

**Abbildungsverzeichnis · Abkürzungsverzeichnis · Literaturverzeichnis · Anhang** (Code-Auszüge, CAD-Zeichnungen,
Rohdaten, Schaltplan) · **Eigenständigkeitserklärung** (Ort, Datum, Name)

## Bewertungskriterien – Zuordnung prüfen
| Kriterium | Kapitel |
|---|---|
| Anforderungsdefinition | 2 |
| Stand der Technik/Forschung, Literaturrecherche | 3 |
| Theoretischer Ansatz | 3 / 4 |
| Systematische Methodik, begründete Lösungsauswahl, technische Entscheidungen | 4 |
| Anteil eigener Ideen | 4 + 5 (explizit benennen) |
| Praktische Durchführung, Funktionsfähigkeit | 4 + 5 |
| Messwerte, Auswertung, Analyse, Evaluation | 5 |
| Softwareablage, technische Dokumentation | 4 + Anhang |
| Selbstständigkeit, Motivation, Teamarbeit | 2 (Tabelle) + 7 |

## Stil und Formalia (abgeleitet aus dem Referenzbericht)
- Fachkapitel sachlich und überwiegend unpersönlich (Passiv/„es wurde …“); Ich-/Wir-Form nur in Kap. 7
  und sparsam am Anfang der Diskussion.
- Jede Abbildung nummeriert, beschriftet und im Text referenziert („siehe Abbildung 3“);
  Unterabbildungen (a), (b), (c) mit `subcaption`; fremde Bilder mit Quellenangabe in der Bildunterschrift.
- Entscheidungen im Muster: Problem → Optionen → Kriterien → Entscheidung → Begründung
  (vgl. im Referenzbericht den Wechsel Arduino → STM32).
- Iterationen sichtbar machen (Versionen mit Abbildungen nebeneinander).
- Diskussion mit konkreten Zahlen und Ursachen statt allgemeiner Aussagen; Datenblätter zitieren.
- Auch Gescheitertes (passive Atemerkennung) sauber als Ergebnis darstellen.
- Abkürzungen beim ersten Auftreten ausschreiben, Abkürzungsverzeichnis per `acro` oder `glossaries`.
- Literatur: biblatex, numerisch [1], mit DOI/URL und „besucht am“; bevorzugt Fachliteratur
  (ACM, IEEE, Frontiers, Sensors/MDPI) + Datenblätter + Vorgängerberichte zu Neffy 2.0.

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
