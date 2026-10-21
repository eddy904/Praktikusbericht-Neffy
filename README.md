# Praktikumsbericht Neffy 3.0 – Team Sensorik

LaTeX-Bericht. Hauptdatei: `main.tex`, ein Kapitel pro Datei in `kapitel/`.

## Einrichtung (einmalig)
1. **MiKTeX** installieren (https://miktex.org) – bei der Installation „fehlende Pakete
   automatisch installieren“ wählen. `pdflatex` und `biber` müssen im PATH sein.
2. **VS Code** öffnen, diesen Ordner öffnen, die empfohlenen Erweiterungen installieren
   (LaTeX Workshop, Claude Code – VS Code fragt automatisch nach).
3. VS Code einmal neu starten.

## Arbeiten
- `Strg+S` in einer `.tex`-Datei kompiliert (pdflatex → biber → pdflatex ×2).
- `Strg+Alt+V` öffnet die PDF-Vorschau.
- Orange Kästen = offene Punkte (`\todo`). Für die Abgabe in `main.tex`
  `\usepackage[disable,...]{todonotes}` setzen.
- Offene Fragen: `OFFENE_PUNKTE.md`. Regeln für Claude: `CLAUDE.md`.

## Ordner
| Ordner | Inhalt |
|---|---|
| `kapitel/` | Kapitel 1–7 + Eigenständigkeitserklärung |
| `anhang/` | Anhang |
| `abbildungen/` | Fotos, CAD, Diagramme |
| `daten/` | Messdaten (Rohdaten) |
| `notizen/` | Notizen, Präsentation |
| `referenz/` | Referenzbericht (nur für Aufbau/Formalia) |
| `.claude/skills/` | Claude-Skills (z. B. PDF) |
