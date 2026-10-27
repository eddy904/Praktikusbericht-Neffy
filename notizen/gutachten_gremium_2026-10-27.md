# Gutachter-Gremium zum Praktikumsbericht (27.10.2026)

Simuliert mit dem Plugin academic-research-skills (academic-paper-reviewer, Modus full), Stand des Berichts:
Commit 282cb1c (46 S., Kap. 1–7 = 32 S.). Fünf Rollen als getrennte Subagenten, die nur den Bericht
(`main.pdf` als Text, LaTeX-Quellen, `daten/`) und nicht die anderen Gutachten sahen.

**Herkunft der Gutachten:** getrennte Kontexte, aber alle auf demselben Modell (Claude, Anthropic) – also
rollengetrennt, nicht unabhängig; gleiche blinde Flecken sind möglich. Die Punktwerte sind eine Simulation,
keine Note.

## Punktschätzung nach Beurteilungsbogen FB VII

| Kriterium | Max | Gesamt | Methodik | Fachgebiet | Praxis | Zusammengefasst |
|---|---|---|---|---|---|---|
| 1 Umfang/Schwierigkeit | 5 | 4–5 | – | – | – | 4–5 |
| 2 Stand der Technik | 10 | 5–7 | – | 5–7 | – | 5–7 |
| 3 Theoretischer Ansatz | 20 | 13–16 | 13–15 | – | – | 13–16 |
| 4 Eigene Ideen | 10 | 6–8 | – | 6–8 | – | 6–8 |
| 5 Praktische Durchführung | 30 | 21–26 | 22–25 | – | 22–25 | 22–25 |
| 6 Auswertung | 10 | 6–8 | 5–7 | – | – | 5–8 |
| 7 Arbeitsstil/Team | 15 | 11–13 | – | – | 11–13 | 11–13 |
| 8 Sonderpunkte | 10 | 5–8 | – | – | 7–9 | 5–9 |
| **Summe** | 110 | 71–91 | | | | **71–91, wahrscheinlich ca. 77–85** |

Notenspanne laut Bogen: 2,3 bis 1,3; am wahrscheinlichsten **2,0 bis 1,7**. Empfehlung aller vier wertenden
Rollen: **kleine Überarbeitung**. Der Advocatus Diaboli fand **kein KRITISCH**: Die Kernaussagen sind im Text
überwiegend ehrlich relativiert.

## Einigkeit (von mehreren Rollen unabhängig genannt)

1. **Tab. 5.1 bewertet stärker, als die Nachweise tragen** (4 Rollen): A1 verlangt eine sitzende Person,
   gemessen wurde eine stehende (je 30 s; „20 min“ nur aus τ = 900 s abgeleitet); A3*/A4 „zuverlässig im
   Betrieb“ ohne Zahl, Messreihen vom Entwicklungsboard mit 10 kΩ; A5 ohne Kraftmessung, obwohl ein
   Stillstand beschrieben ist; A6 ohne Anzahl der Personen und Handmaße.
2. **„Stresslevel“ trägt fachlich nicht** (4 Rollen): Grenzen aus der Ruhenorm, nicht aus Stressliteratur;
   „normal“ umfasst 11–21/min; bewusstes Mitdrücken verändert die Atmung; keine Referenz, ob der Drucktakt
   der Atmung entspricht. 5.4 räumt das ein, aber 2.1, 4.4.4 und 6.1 („passende Übung“) formulieren stärker.
3. **Firmware-Eigenleistung sichtbar machen** (4 Rollen): „Code vollständig mit Claude Code“ ist ehrlich, aber
   der Teamanteil (Spezifikation, Parameter aus eigenen Aufzeichnungen abgestimmt, Testprogramme, Prüfung)
   sollte konkret benannt werden.
4. **Urteil „passiv nicht umsetzbar“ zu allgemein** (Methodik, Advocatus, Fachgebiet): zwei kurze Fenster,
   2 Personen, ungünstiger Arbeitspunkt, kein Referenzgurt → auf den Aufbau beschränken („in den
   Vorversuchen nicht nachweisbar“).
5. **Stand der Technik schmal** (Gesamt, Fachgebiet): nur Neffy-Linie plus Ommie; keine weiteren haptischen
   Atemgeräte, keine Literatur zu Atmung und Stress, Atemerkennung ohne Beispiele/Tabelle, Recherchemethodik
   ohne Zeitraum und Trefferzahlen.
6. **Thermal: „obere Grenze bestätigt“ teils zirkulär** (Methodik, Advocatus): a = 0,4 aus „2 K in 1 m“,
   gemessen 2,7 K (a ≈ 0,54); nur ein Durchgang von fern nach nah, Hysterese beeinflusst 2 m und 3 m.
7. **27 Ω: Verlustleistung nicht betrachtet** (Methodik, Advocatus): bei R_S = R_F ca. 61 mA und 0,1 W je
   Tasche, bei kräftigem Druck bis ca. 0,3 W – für SMD-Widerstände ggf. zu viel. R_S nie gemessen (auch Gesamt).
8. **Läuft der Hub während der 30-s-Messung?** (Fachgebiet, Advocatus): nicht beschrieben; Konflikt mit
   „kräftig drücken“ und Stillstand bei starkem Druck.
9. **Kein Zeitplan/Meilensteine** (Gesamt, Praxis): Arbeitsstil überwiegend Selbstauskunft.

## Einzelbefunde (nur eine Rolle)

- **Praxis:** Sicherheit fehlt ganz (Quetschstellen, Kraftbegrenzung, Kippsicherheit) – als KRITISCH
  eingestuft; Hygiene/Reinigung in der Studie; Kap. 4.3 beschreibt Entscheidungen, begründet sie aber nicht
  (Problem → Optionen → Kriterien); Robustheit (Kabel zu bewegten Teilen, Wärme des Pi im PLA-Kopf);
  Mehrleistung beziffern (Druckzeit, Filament, Kosten).
- **Methodik:** Sensorvergleich ohne definierte Kraft (F1–F3 mit Fingerdruck, R_F unbekannt); „1 kΩ–1 MΩ
  vernachlässigbar“ physikalisch fragwürdig (mit 1 kΩ wäre der FSR abgestuft); F3 hat 36 % Zwischenwerte;
  Auswertefenster manuell gewählt, bei A2 nur 5,5–20 s von 51 s; Spannungen nur nominell (ADC nichtlinear).
- **Gesamt:** „Aufgabenstellung“ und „Durchgeführte Aufgaben“ (Felder im Bogen) als zwei kurze Listen am Ende
  von 2.1; Handmaße besser aus einer Norm (DIN 33402-2); Firmware-Repo nicht als Beleg für physikalische
  Fakten (Datenblätter zitieren); 32 statt ~20 S., kürzbar ohne die Rechnungen.
- **Fachgebiet:** Radar als Kategorie in Tab. 3.1; 5.5 trennt Ideen und Aufgaben nicht scharf (Thermalsensor
  Vorgabe oder Idee? stärkste Idee „aktive Atemtakt-Eingabe“ nicht beansprucht); „Atemgurte vor allem als
  Referenz“ stützt sich auf eine Quelle.
- **Advocatus:** Opportunitätskosten (60 % Gehäuse, 8 % Sensortests) nicht diskutiert; zwei Drücke genügen für
  eine Einstufung; FSR wäre für die aktive Variante passend gewesen; Testpersonen nur das Team; 4.2.4
  („Reserve zeigte sich erst im Betrieb“) vs. 5.4 („wie die Abschätzung erwarten lässt“).

## Uneinigkeit / Abwägung

- **Sicherheit:** nur die Praxis-Rolle sieht ein KRITISCH. Für einen Laborprototyp ohne Bogenkriterium dazu
  eher ein wichtiger Zusatzabsatz als ein Notenrisiko; trotzdem mit wenig Text gut abzudecken.
- **Sonderpunkte:** 5–8 (Gesamt) vs. 7–9 (Praxis); hängt an Fotos und an einer Bezifferung des Aufwands.

## Bestätigte Stärken (mehrere Rollen)

Rechnungen fehlerfrei (von drei Rollen nachgerechnet); Abschätzung und Messung verzahnt; Scheitern der
passiven Erkennung ehrlich und mit Zahlen; Kennwerte aus Rohdaten per Skript reproduzierbar; Fremdleistungen
und KI-Einsatz sauber gekennzeichnet; vollständig aufgebauter, funktionierender Roboter; Gehäuse als echte
Mehrleistung; Velostat-Selbstkritik und Ausblick schlüssig.

## Konflikte mit früheren Entscheidungen (CLAUDE.md / OFFENE_PUNKTE.md)

- Viele Vorschläge sind **neue Messungen am Roboter** (Metronom-Test, Sitztest, Stillstandskraft, Gewichte,
  R_S per Multimeter). Entschieden war: keine weiteren Tests am Roboter, Validierung über die Studie (Eddy).
  Alternative ohne Tests: Status und Formulierungen in Tab. 5.1 und Text ehrlich abschwächen.
- **Stand der Technik erweitern** widerspricht „wird nicht erweitert (Länge); höchstens ersetzen“.
- Literaturvorschläge des Fachgebiets sind **ungeprüft** (vor Aufnahme per DOI prüfen): Haynes et al. 2022
  PLOS ONE 10.1371/journal.pone.0259838; Zaccaro et al. 2018 Front. Hum. Neurosci. 10.3389/fnhum.2018.00353;
  Levinson et al. 2014 Front. Psychol. 10.3389/fpsyg.2014.01202; Sefidgar et al. 2016 IEEE TAC; Miri et al.
  2020 ACM TOCHI; Matheus et al. THRI (Ommie-Journalfassung).

## Priorisierte Maßnahmen

**A – nur Text, ohne neue Tests (größte Wirkung pro Aufwand)**
1. Fotos einsetzen (Abb. 3.1c, 5.1a/b, ggf. Innenleben) – laut Gesamt +3–5 Punkte in Kriterium 5.
2. Tab. 5.1 ehrlich: A1 „stehend statt sitzend“ benennen bzw. „weitgehend erfüllt“; A5/A6 Nachweis
   „qualitativ“; „zuverlässig“ in 5.2.4 nur mit Zahl.
3. „Stresslevel/passende Übung“ in 2.1, 4.4.4, 6.1 zu „grobe Einstufung der Atemfrequenz“ abschwächen.
4. Passive Erkennung auf den Aufbau beschränken; Thermal-Satz „bestätigt“ zu „Messung liegt im bzw. über dem
   Band“.
5. Firmware: Teamanteil konkret benennen (Spezifikation, Abstimmung, Tests).
6. „Aufgabenstellung“ / „Durchgeführte Aufgaben“ als zwei Listen in 2.1.
7. Klarstellen, ob der Hub während der Atemmessung ruht; Auswertefenster in Tab. B.1 offenlegen.
8. Kurzer Absatz Sicherheit und Hygiene; 2–3 Sätze Begründung je Konstruktionsentscheidung in 4.3.

**B – kleine Messungen (nur wenn Eddy die Entscheidung „keine Tests“ öffnet)**
R_S der Taschen per Multimeter; Oberkörper wiegen + Stillstandskraft mit Kofferwaage; Metronom-Test der
Atemerkennung; 10–20 min Sitztest für A1.

**C – Literatur (nur ersetzen, nicht erweitern; vorher prüfen)**
Ein haptisches Atemgerät (z. B. Haynes 2022) und eine Quelle zu langsamer Atmung/Stress (z. B. Zaccaro 2018).
