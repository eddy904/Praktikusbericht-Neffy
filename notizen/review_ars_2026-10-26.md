# Review Praktikumsbericht Neffy 3.0 (ARS academic-paper-reviewer, Modus full) – 26.10.2026

Grundlage: LaTeX-Quellen `kapitel/01–07`, `anhang/anhang.tex`, `daten/tab_kennwerte.tex`,
`daten/Messdaten_Atemsensorik/00_Uebersicht_Kennwerte.csv` + `LIESMICH.txt`,
`anhang/code/BreathingDetection.cpp` (Stand des PDFs vom 26.10., 18:50).
Nicht als Mangel gewertet (Vorgabe): fehlende Fotos (Abb. 3.1c, 5.1), Reichweitenmessung
Thermalsensor, Randnotizen/Platzhalter.

**Ablauf (Provenienz):** Alle fünf Gutachterrollen wurden nacheinander in derselben Sitzung
und mit demselben Modell (Claude Opus 5.5) bearbeitet. Die Rollen sind getrennte Blickwinkel,
aber **keine unabhängigen Gutachten**: Fehler können korreliert sein. Ein menschlicher Gutachter
war nicht beteiligt. Die Bewertung ist nicht kalibriert.

---

## Phase 0 – Einordnung und Besetzung

| Merkmal | Einordnung |
|---|---|
| Textsorte | Praktikumsbericht (Gruppenbericht, 2 Personen), kein Journal-Paper |
| Fach | Humanoide Robotik / Mechatronik; sekundär Mensch-Roboter-Interaktion, Sensorik |
| Paradigma | konstruktiv-technisch (Entwicklung + Erprobung), kleine explorative Messreihen |
| Maßstab | Beurteilungsbogen Praxisphase FB VII (8 Kriterien, 110 Punkte) |
| Reife | weit fortgeschritten, alle Kapitel ausformuliert |

| Sitz | Rolle in diesem Review |
|---|---|
| Journal-Fit (EIC) | Prüferin/Prüfer am FB VII: Passung zum Bogen, Aufgabe, Eigenleistung |
| R1 Methodik | Messtechnik/Versuchsplanung: Messreihen, Prüfkriterien, Evaluation |
| R2 Fachgebiet | Sensorik & Mechatronik: Stand der Technik, Theorie (Gleichungen), Quellen |
| R3 Perspektive | HRI/Ergonomie/Nutzung: Interaktionsdesign, Nutzerperspektive, Studienbezug |
| DA | Advocatus Diaboli: Kernargument, Zirkelschlüsse, Überdehnung |

---

## Gesamturteil

**Überarbeitung empfohlen, in Analogie zu „Minor Revision“.** Der Bericht ist sachlich,
ehrlich und technisch gut belegt; die Gleichungen stimmen (nachgerechnet, s. u.), alle Zahlen
in Kap. 5 stimmen mit der Kennwerte-CSV überein. Neue Versuche sind **nicht** nötig. Die
gewichtigen Punkte betreffen die **Konsistenz zwischen Anforderungen, Prüfkriterien und
Evaluation** (unterschiedlich strenger Maßstab bei ✓), einige **zu starke Formulierungen**
(„zuverlässig“, „robust“, „kostengünstig“, „leiser“) und die **Darstellung der Eigenleistung
bei der Firmware**. Der Stand der Technik ist gemessen an den 10 Punkten des Bogens der
dünnste Teil.

### Einschätzung nach Beurteilungsbogen (qualitativ, keine Punktprognose)

| Nr. | Kriterium | Einschätzung | Wichtigster Hebel |
|---|---|---|---|
| 1 | Umfang/Schwierigkeit | stark | Erweiterung um Gehäuse klar herausgearbeitet (2.1, Abb. 2.2) |
| 2 | Stand der Technik | schwächster Teil | berührungslose Verfahren, Beispiele je Kategorie, Quellen für Abstand/Kamera |
| 3 | Theoretischer Ansatz | gut | Lücken: passive Atemerkennung physikalisch, 27 Ω (Strom/Leistung), Quelle der Gewindeformeln |
| 4 | Eigene Ideen | gut, klar benannt (5.5) | Formulierung Firmware ↔ Claude Code vereinheitlichen |
| 5 | Praktische Durchführung | stark | (Fotos folgen) |
| 6 | Auswertung | solide für die Sensorauswahl, schwach am fertigen System | einheitlicher Evaluationsmaßstab, Nachweisart offenlegen |
| 7 | Arbeitsstil/Team | gut | konkrete Beispiele vorhanden; Zeitaufteilung nur fürs Team |
| 8 | Sonderpunkte | gut begründbar | Gehäuse (60 % der Zeit) ist in den Anforderungen nur mit A6/A7 vertreten |

---

## Stärken (übereinstimmend in mehreren Rollen)

1. **Ehrlichkeit bei Scheitern und Fremdleistung.** Die passive Atemerkennung wird als
   Ergebnis dargestellt (A3 „–“, 5.2.3), A3* ausdrücklich als „im Projektverlauf ergänzt“
   markiert. Board/UART-Bibliothek (Goerke), Kopfmechanik (Jaki) und KI-Einsatz sind offen
   gekennzeichnet. Das ist deutlich besser als im Neffy-2-Bericht.
2. **Theorie mit nachprüfbaren Zahlen.** Nachgerechnet und korrekt: Sichtfeld
   D = 0,47·d (Gl. 4.1), Mischungsmodell und Reichweite 1,4–2 m (Gl. 4.2), Teiler und
   Empfindlichkeitsmaximum U_B/4 bei R_S = R_F (Gl. 4.3/4.4), Steigungswinkel 20,0°,
   η = 0,59–0,75, η' = 0,40–0,69, M = 3–9 Ncm für 20–40 N, 46–59 N bei 10 Ncm (Gl. 4.5–4.9).
   Die Abweichung zwischen Abschätzung (1,4–2 m) und Beobachtung (2–3 m) wird offen benannt.
3. **Entscheidung FSR → Velostat** folgt dem Muster Problem → Optionen → Kriterien →
   Entscheidung und wird mit eigenen Daten **und** Datenblatt (Interlink) erklärt (Abb. 4.4, 4.6).
4. **Reproduzierbarkeit.** Diagramme und Tabelle B.1 werden per Skript aus den Rohdaten
   erzeugt; Firmware-Stand per Commit `2693747` fixiert, Atemerkennung im Anhang.
5. **Kap. 7** ist konkret (Laborzeiten, Druckzeiten, Gehäuse-Entscheidung, „Rückblickend …“).

---

## Konsistenzprüfung Anforderungen ↔ Prüfkriterium ↔ Nachweis ↔ Status

| Nr. | Prüfkriterium (Tab. 2.1) | Nachweis im Bericht | Status (Tab. 5.1) | Befund |
|---|---|---|---|---|
| A1 | Person auf dem Platz erkannt; leerer Platz: keine Anwesenheit | Beobachtung im Betrieb | (✓) | Kriterium enthält weder Dauer noch Abstand, obwohl die Anforderung „kaum bewegt“ betont; Konflikt mit dem 20-s-Neulernen (→ M3) |
| A2 | Meldung bei jeder Änderung, spätestens alle 0,5 s | Firmware-Verhalten | ✓ | Kriterium prüft den Sendetakt, nicht die Verzögerung der Erkennung selbst; Nachweisart (Code/UART-Monitor) nennen |
| A3 | Einatemzüge vom Rauschen unterscheidbar | P1, P2 (Entwicklungsboard, 10 kΩ, Sichtprüfung) | – | Aussagekraft begrenzt (→ M4) |
| A3* | Einatemzüge bei aktivem Drücken klar erkennbar | A1–A6 offline am Entwicklungsboard; am Roboter beobachtet | ✓ | gleiche Nachweisart am Roboter wie A1, aber anderer Status (→ M1) |
| A4 | Einstufung kommt am Pi an | Betrieb | ✓ | passt; „Grenzen nicht validiert“ steht korrekt dabei |
| A5 | Hub mit beiden Händen ohne Stocken | Beobachtung | ✓ | keine Last genannt; „starkes Drücken“ nicht beziffert |
| A6 | Taschenmaße vs. Literatur; verschiedene Handgrößen passen, rutschen nicht ab | Tab. 4.2; „mit verschiedenen Handgrößen geprüft“ | ✓ | Anforderung sagt „angenehm“, Schwachstelle „Ellbogen zu hoch“ widerspricht teilweise; Anzahl/Größen der Probehände fehlt; Taschenlänge 20 cm ≈ P95-Handlänge 19,9–20,0 cm (kein Spielraum) |
| A7 | Schultern/Kopfdeckel ohne Werkzeug, Unterkörper verschraubt | Konstruktion | ✓ | stimmig mit Tab. 4.3 |
| A8 | Klicks und Auswahl werden erkannt | Betrieb | ∘ | stimmig |
| – | *Ziel „deutlich leiser“ (2.1, 4.2.4)* | keiner | – | Ziel ohne Anforderung und ohne Nachweis (→ M7) |

---

## Hauptpunkte (gewichtig, aber ohne neue Versuche lösbar)

**M1 – Uneinheitlicher Maßstab in Tab. 5.1** (R1, EIC, DA)
A1 erhält „(✓) vorläufig“, weil nur beobachtet. A3*, A5 und A6 erhalten „✓“, obwohl der
Nachweis am fertigen Roboter ebenfalls nur Beobachtung ist (5.2.4: „Erkennungsrate nicht
systematisch bestimmt“). Eine Prüferin kann das als zu günstige Bewertung lesen.
*Vorschlag:* In Tab. 5.1 eine Spalte **„Nachweis“** (Messung / Beobachtung / Firmware) ergänzen
und in der Legende festlegen, was ✓ bedeutet. Dann darf A3* ✓ bleiben, wenn „Messung am
Entwicklungsboard + Beobachtung am Roboter“ dasteht; alternativ A3*/A5 auf (✓) setzen.

**M2 – Prüfkriterien teils unschärfer als die Anforderung** (R1)
A1 (Dauer fehlt), A2 (Sendetakt ≠ Verzögerung), A3* („klar erkennbar“), A5 (Last fehlt),
A6 („angenehm“ im Kriterium nicht geprüft). Kriterien nachträglich zu verschärfen wirkt
schlecht; besser in der Begründungsspalte offenlegen, *wie* geprüft wurde.
*Vorschlag:* A5: Last nennen, falls bekannt (z. B. „beide Hände ruhend aufgelegt“, Bezug zu
den 2–4 kg aus Neffy 2). A6: Status ∘ oder aufteilen („gesichert ✓, Ergonomie ∘“) und
Anzahl/Spannweite der Probehände nennen, falls bekannt.

**M3 – Argumentationskonflikt bei der Anwesenheitserkennung** (DA, R2, R3)
Kap. 3 (Tab. 3.1) und 4.2.1 begründen den Thermopile gerade damit, dass er still sitzende
Personen erkennt. In 4.4.2 wird die Raumtemperatur aber neu gelernt, wenn das Signal 20 s
nahezu konstant bleibt, „da eine reale Person die Messung innerhalb von Sekunden verändert“.
Diese Annahme widerspricht der Prämisse – und eine ruhig sitzende Person während einer
Atemübung ist genau der Anwendungsfall. Das ist kein Messmangel, sondern eine
Argumentationslücke, die schon jetzt geschlossen werden kann.
Dazu: Der Einpixelsensor kann „sitzt vor Neffy“ und „geht in 2 m vorbei“ nicht unterscheiden;
A1 spricht aber von „Person auf dem Platz“.
*Vorschlag:* In 4.4.2 als bewussten Zielkonflikt benennen (Schutz vor Wärmequellen vs.
Erkennung sehr ruhiger Personen) und sagen, was „nahezu konstant“ heißt (Schwelle relativ zum
Rauschen?). Einen Satz ergänzen, ob/wie der Pi Sitzen und Vorbeigehen unterscheidet (z. B.
über die Dauer) – oder dass er es nicht tut.
Außerdem 4.2.1: „Ein Vergleichstest entfiel, da bereits der D6T die Anforderungen erfüllte“
stützt sich auf A1, das selbst nur vorläufig erfüllt ist → „… im Betrieb erfüllte“.

**M4 – Negativbefund passive Atemerkennung schmaler belegt, als Kap. 1/6 nahelegen** (DA, R1)
Belegt durch zwei Messreihen, zwei Personen, Entwicklungsboard, 10 kΩ mit Plateau nahe dem
oberen Messbereich (5.2.3 sagt selbst: mit angepasstem Widerstand empfindlicher), Beurteilung
per Sichtprüfung, ohne Referenz der tatsächlichen Atemfrequenz. Die neuen, größeren Einsätze
mit 27 Ω wurden nie passiv getestet. 5.2.3 formuliert korrekt „mit diesem Aufbau“; Einleitung
(„mit der gewählten Sensorik“) und Fazit verallgemeinern stärker.
*Vorschlag (nur Datenauswertung, keine neue Messung):* Spektrum von P1/P2 im Atemband
0,1–0,5 Hz zeigen (kein Peak = deutlich stärkeres Argument als Sichtprüfung). Dazu 2–3 Sätze
zur Physik: Die Hände liegen auf dem Roboter, die Atembewegung des Brustkorbs überträgt sich
über Schulter und Arm kaum als Kraftänderung auf die Hand. Den Geltungsbereich in Einleitung
und Fazit an 5.2.3 angleichen.

**M5 – Aktive Erkennung: Auswertung ≠ Firmware** (R1)
A1–A6 wurden offline mit Peak-Erkennung (Mindesthöhe 700, „für die aktiven Messreihen
gewählt“) ausgewertet; die Firmware nutzt dagegen den Zustand „gedrückt“ (140/200 ms) mit
selbstkalibrierten Schwellen, andere Einsätze und 27 Ω. Die Schwelle wurde an denselben Daten
gewählt, die sie bestätigen; die wahre Zahl der Atemzüge je Messreihe ist nicht bekannt.
*Vorschlag:* Einen Satz ergänzen, dass die Offline-Auswertung die **Signalqualität** belegt,
nicht die Firmware-Erkennung. Das steht in 5.2.4 schon ansatzweise und sollte auch in die
Begründung von A3* in Tab. 5.1.

**M6 – 27 Ω: Faktor ~370 und Verlustleistung nicht diskutiert** (R2)
Von 10 kΩ auf 27 Ω ist ein Faktor ~370. Mit „Widerstand sinkt mit der Fläche“ lässt sich das
nur erklären, wenn die Fläche entsprechend gewachsen ist; die Fläche des Testsensors ist nicht
angegeben. Zudem folgt aus Gl. 4.3: bei R_S = R_F = 27 Ω fließen 3,3 V / 54 Ω ≈ 61 mA je
Tasche (P_RF ≈ 0,10 W); bei R_S → 0 bis 122 mA und 0,40 W im Festwiderstand – mehr als ein
üblicher ¼-W-Widerstand verträgt, und zwei Taschen belasten die 3,3-V-Versorgung mit bis zu
~0,25 A. „feiner aufgelöst“ ist nicht belegt.
*Vorschlag:* Fläche alt/neu nennen, Strom und Leistung kurz rechnen (passt zum Kriterium
„Theoretischer Ansatz“) und Belastbarkeit des Widerstands bzw. der Versorgung angeben –
**bitte am Aufbau prüfen**, ob das real ein Problem ist. „feiner“ entweder begründen oder
streichen.

**M7 – Einige Aussagen stärker als die Belege** (DA, EIC)
- 3.5: „robuste Einschätzung der Atemfrequenz“ → „einfache Einschätzung“.
- 6.1: „Die aktive Erfassung funktioniert dagegen zuverlässig“ → „funktionierte in allen
  Messreihen und im Betrieb“.
- 5.1: „Alle Funktionen … arbeiten“ – A8 ist nur ∘.
- 6.1: „kostengünstige Sensorik“ – beziffert ist nur der D6T (16 €). Kurze Kostenzeile
  (D6T, Velostat, Kupferfolie) oder Wort streichen.
- 2.1/4.2.4: „deutlich leiser“ – Ziel ohne Anforderung und ohne Nachweis, obwohl Lautstärke
  eine benannte Schwäche von Neffy 2 war. Entweder als Beobachtung kennzeichnen oder als
  offenen Punkt in 5.4 aufnehmen.

**M8 – Eigenleistung Firmware uneinheitlich formuliert** (EIC, DA)
Tab. 2.2: „Firmware des ESP32-S3 … Younes Jamil“; Kap. 7: „hat die Firmware … vollständig
aufgesetzt“; 4.4.7: „Der Quellcode … wurde vollständig mit Claude Code geschrieben“. Einzeln
korrekt, zusammen liest es sich widersprüchlich – bei einem Bewertungskriterium „Anteil
eigener Ideen“ ist das heikel.
*Vorschlag:* Überall gleich formulieren, z. B. „Konzeption, Inbetriebnahme und Test der
Firmware (Code mit Claude Code, Abschnitt 4.4.7)“.

**M9 – Stand der Technik dünn für 10 Punkte** (R2, R3)
- Berührungslose Verfahren: ein Satz ohne Beispiel (Radar, Kamera, Wärmebild) – obwohl
  `massaroni2021contactless` genau das liefert.
- Abstand- und Kamera-Punkt in 3.3 ohne Quelle.
- „Roboter für Atemübungen“ nur Ommie und Neffy; mindestens ein weiteres haptisches
  Interaktionsobjekt würde die Einordnung stärken (Vorschlag: Yohanan & MacLean 2012,
  Haptic Creature, IJSR – im Index gefunden, Inhalt vor Aufnahme prüfen).
- Velostat nur über eine Shop-Seite belegt; eine Fachquelle zu piezoresistiven Folien wäre
  besser (Suchbegriffe: „Velostat pressure sensor characterization“, „piezoresistive polymer
  composite tactile sensor“).
- Gewindeformeln (Gl. 4.6–4.9) ohne Lehrbuchquelle → z. B. Roloff/Matek Maschinenelemente
  (im Index gefunden; Auflage/Seiten selbst prüfen).
- 3.1 nennt als Einschlusskriterium „begutachtete Veröffentlichungen mit DOI sowie
  Datenblätter“; Waveshare-/Adafruit-Produktseiten und der interne Neffy-2-Bericht passen
  nicht dazu → „… sowie Datenblätter, Herstellerangaben und die Vorgängerberichte“.

---

## Kleinere Punkte

- 4.3.3: „Nur am Kopf wird das Hinterteil … verschraubt“ – widerspricht der verschraubten
  hinteren Klappe des Unterkörpers (Tab. 4.3, Tab. 5.1).
- 4.3.3: „vollständig zerlegen“ – Ober-/Unterkörper sind verklebt → „in seine Baugruppen zerlegen“.
- 2.1: zwei Sätze hintereinander mit „Zudem“.
- 1: Der Einstiegssatz „Stress betrifft sehr viele Menschen“ ist unbelegt (Quelle oder vorsichtiger formulieren).
- 4.2.3: Handmaße aus Kolumbien/China – für Mitteleuropa gibt es DIN 33402-2 (Körpermaße);
  optional als Ergänzung.
- 4.2.4: Entscheidung Spindel vs. Riementrieb (Neffy 2) fehlt im Muster Optionen → Kriterien.
  Gerade weil die Spindel *nicht* selbsthemmend ist, sollte kurz stehen, was für sie sprach
  (Untersetzung/Kraft, Geräusch, Bauraum, Verfügbarkeit).
- 4.2.4/5.4: Motormoment unbekannt – ein Datenblatt eines vergleichbaren NEMA-17-Motors mit
  kurzer Bauform würde die Größenordnung liefern (als „vergleichbarer Typ“ kennzeichnen).
- Anhang B: Kürzung der Ruhephase (F2, P1) und herausinterpolierte Störspitzen (A6) stehen
  nur in `LIESMICH.txt` – ein Satz im Anhang genügt.
- Öffentliche CSV: Spalten „Bezeichnung im Chat“ und „Zuordnung: … bitte prüfen“ (P1/P2) sind
  veraltet, laut `LIESMICH.txt` am 21.10. bestätigt → vor Abgabe bereinigen.
- 2.3: Zeitaufteilung nur fürs Team; die Gliederung nennt „pro Person“. Ein Satz „beide etwa
  gleich, Schwerpunkte siehe Tab. 2.2“ ist da, reicht vermutlich.
- 5.4 (Interaktion): Bei der aktiven Erkennung lernen die Nutzer:innen „beim Einatmen
  drücken“; in der Übung hebt der Roboter beim Einatmen. Drücken sie aus Gewohnheit weiter,
  trifft das die bekannte Grenze des Antriebs (A5). Ein Satz dazu wäre sinnvoll, falls das
  beobachtet wurde.

---

## Advocatus Diaboli

**Stärkstes Gegenargument.** Neffy 3.0 erfasst keine Atmung, sondern eine willentliche
Eingabe im Atemtakt. Die Nutzer:innen werden aufgefordert, beim Einatmen zu drücken; die
gemessene „Atemfrequenz“ ist damit die Frequenz, mit der eine Person drückt, während sie weiß,
dass sie dabei beobachtet wird – und bewusstes Atmen verlangsamt typischerweise. Die
Einstufung „gestresst“ (> 21/min) kam in keiner Messreihe vor (alle 9,7–15,2/min, nur
Teammitglieder), ist also nie aufgetreten. Die Anforderung wurde nach dem Scheitern angepasst
(A3 → A3*), und A3* wird mit Daten belegt, die mit anderem Sensoreinsatz, anderem
Festwiderstand, anderer Hardware und einem anderen Algorithmus entstanden sind als im
fertigen Roboter. Schließlich empfiehlt der Ausblick, Velostat durch einen Taster zu ersetzen:
Das Kriterium, mit dem Velostat in Tab. 4.1 gewonnen hat (abgestufter Verlauf), spielt für die
umgesetzte Funktion keine Rolle mehr. Die Bewertungsmatrix hat also auf eine Funktion hin
optimiert, die am Ende nicht umgesetzt wurde.

**Abwägung.** Der Bericht verschweigt keinen dieser Punkte: 1, 5.2.4, 5.4 und 6.2 benennen
die bewusste Mitwirkung, die fehlende Validierung, den Einfluss des Mitdrückens auf die Atmung
und den Taster. Die Sensorauswahl fiel, als die passive Erkennung noch Ziel war – das ist
nachvollziehbar und kein Fehler. Daher **kein CRITICAL-Befund**; der Punkt geht als M4, M5,
M7 in die Liste ein. Was fehlt, ist ein Satz, der die Matrix ausdrücklich in diesen
zeitlichen Zusammenhang stellt (4.2.2 oder 5.4).

**Weitere DA-Befunde:** Zirkel bei M3 (Begründung des Vergleichsverzichts durch eine vorläufig
erfüllte Anforderung); Selektion der Messreihen ist offengelegt (A5 als „beste“ in Abb. 4.4) –
in Ordnung, weil Tab. B.1 alle zeigt.

**Fehlende Perspektiven:** Nutzer:innen außerhalb des Teams (alle Messreihen mit zwei
Teammitgliedern); Menschen mit eingeschränkter Handkraft oder Feinmotorik, für die Drücken im
Atemtakt schwerfällt; Zielgruppe „Kinder“ (Einleitung) bei 43 × 45 cm Gehäuse und hoher
Handposition.

---

## Überarbeitungsplan (Vorschlag; Reihenfolge nach Aufwand/Nutzen, Entscheidung beim Team)

| # | Maßnahme | Ort | Aufwand |
|---|---|---|---|
| 1 | Spalte „Nachweis“ in Tab. 5.1 + Legende für ✓ | 5.3 | klein |
| 2 | Firmware-Eigenleistung einheitlich formulieren | Tab. 2.2, 4.4.7, 7 | klein |
| 3 | Überformulierungen entschärfen (robust, zuverlässig, alle Funktionen, kostengünstig, leiser) | 3.5, 5.1, 6.1, 2.1, 4.2.4 | klein |
| 4 | Zielkonflikt 20-s-Neulernen vs. ruhiges Sitzen benennen; Sitzen/Vorbeigehen; Satz zum Vergleichstest | 4.2.1, 4.4.2 | klein |
| 5 | A6 Ergonomie im Status abbilden; Probehände nennen | Tab. 5.1 | klein |
| 6 | 27 Ω: Flächen nennen, Strom/Leistung rechnen, Belastbarkeit am Aufbau prüfen | 4.2.3 | mittel |
| 7 | Spektrum P1/P2 aus vorhandenen Daten; Geltungsbereich in 1/6 angleichen | 5.2.3, 1, 6 | mittel |
| 8 | Stand der Technik: berührungslose Beispiele, Quellen Abstand/Kamera, ein weiteres haptisches Objekt, Fachquelle Velostat, Lehrbuch Gewinde, Einschlusskriterien | 3, 4.2.4 | mittel |
| 9 | Kleinere Punkte (Klappe, „zerlegen“, „Zudem“, Anhang B, CSV bereinigen) | diverse | klein |

---

## Anhang: Prüfskripte

**Literaturvorschläge (Skript `verify_panel_recommendations.py`, Ausgabe unverändert):**

```
| R2 | 1 | Dzedzickis, A. (2020) "Polyethylene-Carbon Composite (Velostat) Based Tactile Sensor" | Title not matched; no DOI or arXiv ID to check |
| R2 | 2 | "Roloff/Matek Maschinenelemente" | Found in an index |
| R3 | 1 | Yohanan, S. et al. (2012) "The Role of Affective Touch in Human-Robot Interaction: Human Intent and Expectations in Touching the Haptic Creature" | Found in an index |
"Found" means an index holds a record ... It does not show that the work supports the recommendation.
```
Der Dzedzickis-Titel wurde nicht gefunden und wird deshalb **nicht** als Quelle empfohlen
(nur Suchbegriffe in M9).

**Abkürzungsprüfung:** nicht ausgeführt (Skript unterstützt nur en/zh-TW; das `acro`-Paket
schreibt Abkürzungen ohnehin beim ersten Auftreten aus).

**Abgleich der Gutachterbefunde mit dem Text (Claim-Check):** Der separate Prüfschritt wurde
nicht ausgeführt. Stattdessen sind alle Zahlen aus Kap. 4/5 und Tab. B.1 von Hand mit der CSV
und den Gleichungen abgeglichen worden; Abweichungen wurden keine gefunden.
