# Analyse: Praxisbericht Neffy 2 (`referenz/Praxisbericht.pdf`)

**Was es ist:** Praxisbericht zu **Neffy 2**, also der Vorgängerversion unseres Projekts.
Autor:innen: Charly Goerke (Konstruktion) und Jessica Kazubski (Programmierung).
Erstellt im Labor für Kommunikation, BHT. Lehrkraft: Prof. Dr. Ilona Buchem, Betreuer: Prof. Dr. Manfred Hild.
Abgabe am 11.03.2025, 33 Seiten, mit LaTeX/MiKTeX gesetzt.
Es ist **nicht** der in `CLAUDE.md` genannte Headset-Lift-Bericht.

Der Bericht ist für uns damit zweierlei:
1. **Zitierbare Quelle** und **Ausgangspunkt** für Neffy 3.0 (Kap. 2 und 3), eingetragen als `goerke2025neffy2`.
2. **Formale Vorlage** aus demselben Labor und bei derselben Lehrkraft.

## Gliederung
1 Vorwort · 2 Allgemeines (Einbettung, Arbeitsaufteilung, Zeitaufteilung, Vorgänger,
Funktionsweise) · 3 Aufbau des Roboters (Antrieb, Kopf, Körperschale, Elektronik) ·
4 Software (Pi, Display, Motoren, Lautsprecher, Autostart, Interaktionsskript) ·
5 Demontage-/Montageanleitung · Abbildungs-/Tabellenverzeichnis · Literatur

Der Bericht ist eher eine technische Dokumentation als ein wissenschaftlicher Bericht.
Es fehlen: Anforderungen, Stand der Technik, Diskussion, Fazit, Ausblick, Einschätzung
und Eigenständigkeitserklärung. Der Code wird als „im Anhang“ angekündigt, ein Anhang
ist im PDF aber nicht enthalten.

## Formalia
| Merkmal | Neffy 2 | Für uns |
|---|---|---|
| Titelblatt | BHT-Vorlage: Logo oben rechts, BHT-Formen, „Studiere Zukunft“; Titel, Labor, Namen + Matr.-Nr., Lehrkraft, Betreuer, Studiengang, Abgabedatum | BHT-Logo/Vorlage besorgen; Felder „Lehrkraft“ und „Betreuer“ übernehmen |
| Kopfzeile | links Kapitel, rechts „Praxisbericht Neffy 2“; Seitenzahl unten mittig | gleich umsetzen (scrlayer-scrpage) |
| Schrift/Satz | Serifenschrift, Blocksatz, A4, einspaltig | entspricht unserem Gerüst |
| Abbildungen | nummeriert, (a)/(b) nebeneinander, im Text referenziert; farbige CAD-Renderings | so beibehalten |
| Gleichungen | nummeriert, mit Herleitung und eingesetzten Datenblattwerten | Vorbild für eigene Rechnungen |
| Tabellen | eine (Strombudget) | wir brauchen deutlich mehr |
| Literatur | numerisch, gruppiert (Konstruktion / Programmierung / Datenblätter), „besucht am“ | numerisch ja; Gruppierung optional |
| Quellenart | fast nur Webseiten und Datenblätter, keine Fachliteratur | wir zusätzlich: Fachartikel (Kap. 3) |
| Tonfall | sachlich, überwiegend Passiv; vereinzelt „wir“; „Benutzer*innen“ | Passiv ja; Gendern einheitlich festlegen |
| Verzeichnisse | Abb.- und Tab.-Verzeichnis am Ende; keine Abkürzungen | wie geplant, plus Abkürzungsverzeichnis |

## Was wir übernehmen sollten
- **Arbeits- und Zeitaufteilung pro Person:** 5 Monate, 450 h pro Person, Tortendiagramm nach
  Arbeitsbereichen. Das eignet sich für Kap. 2.4 und das Titelblatt („Dauer“).
- **Rechnung mit Datenblattwerten:** Drehmoment → maximal hebbare Masse, mit 70-%-Reserve,
  dazu eine Strombudget-Tabelle. Das stützt „Theoretischer Ansatz“ und „technische Entscheidungen“.
- **Empirische Toleranz:** Der Zahnrad-Achsabstand wurde rechnerisch zu 34 mm bestimmt und
  experimentell auf 33,3 mm korrigiert. Das ist genau unser Muster mit den FDM-Toleranz-Testkörpern.
- **Vergleich mit dem Vorgänger:** Bilder nebeneinander plus Liste der Änderungen.
- **Farbcodiertes Blockschaltbild** (Stromversorgung, Audio, Video, Motor).
- **Demontage-/Montageanleitung:** als Anhang für unser Gehäuse (technische Dokumentation).

## Was wir besser machen müssen
- Lösungsauswahl begründen: Neffy 2 nennt Spindel- vs. Riementrieb ohne Kriterien und ohne Bewertung.
- Anforderungen, Messwerte, Evaluation, Schwachstellen und Ausblick fehlen bei Neffy 2 ganz.
- Softwareablage: Repo-Link statt Installationsbefehlen im Fließtext.

## Inhaltlich relevant für uns (Stand Neffy 2 = Ausgangspunkt)
- Bewegung: **Schultern** heben und senken sich über einen Riementrieb (max. 25 mm Hub), der **Kopf**
  nickt über Zahnräder. Dafür gibt es 2× Dynamixel XL430-W250, U2D2 + Power Hub.
- Die Nutzer:innen legen die **Hände auf die Schultern** (haptischer Atemtakt). Das ist der
  Hintergrund für unsere passive Atemerkennung.
- Steuerung: Raspberry Pi 4B mit Python. Display ILI9488 mit Touch (XPT2046), Lautsprecher, 12-V-Netzteil.
- Touch: nur über den Touchscreen (Menüs für Lautstärke, Dauer, Wiederholen; Skip-Funktion).
- Atemzyklus: 4 s ein, 0,5 s Pause, 5 s aus, 0,5 s Pause, also 10 s. Übungsdauer 1, 3 oder 5 min.
- Neffy 2 hat keine Sensoren für Anwesenheit oder Atmung. Genau hier setzt Neffy 3.0 an.
- Vorgänger Neffy 1: Bericht von Dincel & Thomas (April 2024), dort zitiert als [1].
  Noch nicht beschafft.

## Geklärt (21.10.2026)
- Der Bericht ist die Vorlage für Titelblatt und Formalia. Das Titelblatt ist umgesetzt.
- Wir arbeiten ebenfalls im Labor für Kommunikation. Lehrkraft ist Prof. Buchem;
  Prof. Hild ist Studiengangsleiter (wer als Betreuer eingetragen wird, ist noch offen).
- Neffy 3.0 baut auf Neffy 2.0 auf: Der Pi und die Schulter- und Kopfbewegung bleiben,
  die Dynamixel-Motoren wurden ersetzt.

## Offen
- Durch welche Motoren wurden die Dynamixel ersetzt?
- Heißt es bei uns „Praxisbericht“ oder „Praktikumsbericht“?
