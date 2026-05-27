---
name: dashboard-style
description: Ein poliertes, redaktionelles Light-Mode-Designsystem für HTML-Dashboards, Briefings, Berichte und visuelle Seiten. Liefert eine saubere redaktionelle Farbpalette (gebrochenes Weiß als Hintergrund, fast-schwarzer Text, graue Akzente, kein Orange) – adaptiert vom PDF-Guide-Skill. Verwende diesen Skill immer bei der Erstellung von HTML – Dashboards, Briefings, Berichte, Wrapups, Analyseseiten, visuelle Erklärseiten, Audit-Panels, Pipeline-Übersichten, Ressourcen-Landingpages. Trigger-Begriffe: "dashboard", "briefing", "bericht", "html-seite", "visuelle seite", "tagesabschluss", "wrapup", "morgen-briefing", "stats", "analytics", "auswertung".
---

# Dashboard Style

Ein House-Design-System für HTML-Seiten. Wird mit einer Standard-Editorial-Light-Palette und einem Serif/Sans-Typo-Paar ausgeliefert – alles davon kann auf Wunsch gegen eigene Markenfarben ausgetauscht werden (z. B. „Verwende meine Markenfarben: #XYZ und #ABC" oder „Ersetze die Serif-Überschriften durch Poppins Bold").

## Wann verwenden

**Standard für HTML-Ausgaben.** Morgen-Briefings, Wrapups, Pipeline-Übersichten, Research-Dashboards, Stats-Seiten, Analyseberichte, Audit-Panels, visuelle Erklärseiten, Ressourcen-Landingpages – alles davon. Ausnahmen:
- Präsentationen/Slideshows → eigenen Slideshow-Skill verwenden
- PowerPoint `.pptx` → pptx-Skill verwenden
- Einzelne statische Infografiken → Image-Generation-Skill verwenden

## Anpassung an eigene Marke

Dieser Skill liefert sinnvolle Standardwerte, alles davon kann überschrieben werden:
- **Farben:** „Verwende meine Markenfarben – Navy #0a2540 und Lime #c6f432" → Skill verwendet diese statt der Standardwerte
- **Schriften:** „Verwende Inter für alles" oder „Verwende Playfair Display für Überschriften"
- **Modus:** „Mach es Dark Mode" → Skill kehrt Hintergrund/Oberfläche-Verhältnis um
- **Animation:** „Keine Animationen" → Skill entfernt Spin- und Puls-Effekte
- **Signalfarbe:** „Füge einen Teal-Akzent hinzu" → Skill verwendet diese Farbe für Highlights, Zahlen und Badges

Wenn nichts spezifiziert wird, gelten die folgenden Standardwerte.

## Standard-Design-Tokens

### Farben (redaktionelles Light-Default – adaptiert vom PDF-Guide-Skill)
```
--bg: #f8f7f3             /* gebrochenes Weiß als Seitenhintergrund */
--bg-2: #f5f5f5           /* leicht angehobene Oberfläche (Callout-Boxen) */
--surface: #ffffff         /* weißer Karten-Hintergrund */
--surface-hover: #f5f5f5  /* Karte bei Hover */
--surface-dark: #2d2d2d   /* dunkle Panels, Prompt-Blöcke */
--border: #e0e0e0         /* helle Umrandung auf weißen Karten */
--border-dark: #b0b0b0    /* Akzent-Umrandung / Trennlinien */
--text-dark: #1a1a1a      /* primärer Fließtext */
--text-light: #f8f7f3     /* Fließtext auf dunklen Panels */
--text-secondary: #7a7a7a /* Meta-Text, Footer, Bildunterschriften */
--text-muted: #b0b0b0     /* unterstützende Akzente */
--accent: #1a1a1a         /* fast schwarz – Signal/Highlight */
--accent-light: #2d2d2d   /* leicht helleres Signal */
--accent-dark: #000000    /* reines Schwarz für maximalen Kontrast */
--accent-glow: rgba(26, 26, 26, 0.06)
--accent-bg: #f5f5f5      /* getönter Hintergrund für Badges/Tags */
```

### Typografie (Standard)
- **Überschriften:** `'Instrument Serif', Georgia, serif` – Stärke 400, enger Buchstabenabstand, ein Wort pro Überschrift kursiv in hellerem Ton (z. B. „Dein *tägliches* Briefing")
- **Fließtext:** `'Poppins', -apple-system, sans-serif` – Stärken 400/500/600/700
- **Monospace:** `'SF Mono', 'Fira Code', monospace` – für Slash-Befehle, Code
- **Hero h1 Größe:** `clamp(36px, 5vw, 62px)`

### Google Fonts Import
```html
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
```

## Visuelle Signalelemente (Standard – optional)

1. **Starburst-SVG-Marke** – dekoratives Sonnen-/Funken-Icon im Header. Dreht sich langsam (20s). Kann durch eigenes Logo-SVG ersetzt werden. Füllfarbe: `#1a1a1a`.
2. **Badge mit pulsierendem Punkt** – kleines dunkles Pill-Element oben mit pulsierendem Punkt. Für Zeitstempel oder Live-Status. Hintergrund: `--accent-bg`, Text: `--text-secondary`.
3. **Kursiver Akzent in jeder Überschrift** – ein Wort pro Überschrift kursiv in `--text-secondary` (grau).
4. **Unterstrichene Abschnittsüberschriften** – h2 erhält `border-bottom: 0.75px solid var(--text-dark)` für redaktionelles Feeling.
5. **Callout-Box** – gebrochenes Weiß als Hintergrund (`--bg-2`), fetter schwarzer linker Rand (2px), kleines Großbuchstaben-Label über kursivem Fließtext.
6. **Dunkle Panels** (`--surface-dark: #2d2d2d`) – für Prompt-Blöcke, Projektkarten oder eingebettete Bereiche, die visuellen Kontrast zur hellen Seite brauchen.

> Hinweis: Keine Ambient-Orbs oder Glow-Effekte – der redaktionelle Light-Stil ist bewusst flach und klar.

## Standard-Seitengerüst (empfohlene Reihenfolge)

1. **Header** – Logo/Marke + Wortmarke + Badge + Serif-h1 + Untertitel + Stats-Bar + Trennlinie
2. **Hauptinhalt** – der Dashboard-Body (Abschnitte, Karten, Metriken)
3. **Footer** – kleine zentrierte Kreditzeile in Großbuchstaben, gedämpfter Farbe

## Standard-Muster

1. Gebrochenes Weiß als Seitenhintergrund mit weißen Karten darauf.
2. Signalfarbe ist fast-schwarz `#1a1a1a` – für Zahlen, Unterstreichungen, Badge-Punkte und Icon-Konturen. Niemals flächig einfärben.
3. Eine Serif für Überschriften, eine Sans für Fließtext – sauber kombinieren.
4. Abgerundete Ecken: Karten = 10px, Pills = 100px, Eingabefelder = 8px.
5. Dezente Animationen: `fade-in` für Abschnitte, `spin-slow` für das Logo-Marke, `pulse-dot` für Badges.
6. Rahmen immer `0.75px` – haarfein, niemals schwer.
7. Metrik-Unterzeilen verwenden semantische Farbe für Auf/Ab: Grün (`#3a7d44`) für positiv, Rot (`#9b3535`) für negativ.

## Inhalt nach Dashboard-Typ

- **Morgen-Briefing:** Badge (`Morgen-Briefing`), Hero („Dein *tägliches* Briefing"), Stats-Bar (E-Mails/Kalender/Prioritäten), Callout-Box für Top-Insight, Karten-Grid für Prioritäten.
- **Pipeline-Dashboard:** Badge (`Pipeline`), Hero („*Content* Pipeline"), Stats-Bar (veröffentlicht/bereit/gefilmt/Ideen), Karten-Grid nach Status gruppiert.
- **Wrapup / Tagesabschluss:** Badge (`End of Day`), Hero („Heutiger *Rückblick*"), Stats-Bar (Erfolge/gefilmt/veröffentlicht/umgesetzt), Kategorienabschnitte.
- **Research / Analytics:** Badge (`Research`), Hero mit kursiv gesetztem Thema, Stats-Bar mit Schlüsselmetriken, Ergebnisse als Karten.
- **Audit / Wochenreview:** Metrik-Karten mit Auf/Ab-Unterzeilen, dunkle Panels mit Fortschrittsbalken, Callout-Box für zentrale Empfehlung.

## Komponenten-Referenz

### Stats-Bar
```html
<div class="stats-bar">
  <div class="stat-item">
    <span class="stat-num">12</span>
    <span class="stat-label">neue E-Mails</span>
  </div>
</div>
```
CSS: `stat-num` bei 26px/600 in `--text-dark`, `stat-label` bei 11px Großbuchstaben in `--text-secondary`.

### Weiße Karte (hell)
```html
<div class="card">
  <div class="card-icon"><!-- SVG-Icon --></div>
  <div class="card-title">Titel</div>
  <div class="card-desc">Beschreibung</div>
  <div class="card-meta">
    <span class="card-tag">Label</span>
    <span class="card-date">10:00 Uhr</span>
  </div>
</div>
```
CSS: weißer Hintergrund, `--border`-Rahmen, 10px Radius, Hover zu `--surface-hover`.

### Dunkles Panel (für Projekte, Prompts, eingebettete Bereiche)
```html
<div class="dark-card">
  <div class="dark-card-title">Titel</div>
  <div class="dark-card-text">Text</div>
  <div class="progress-row">
    <div class="progress-label"><span>Fortschritt</span><span class="progress-val">68 %</span></div>
    <div class="progress-bar"><div class="progress-fill" style="width:68%"></div></div>
  </div>
</div>
```
CSS: `--surface-dark`-Hintergrund, weißer Titel, grauer Fließtext, gebrochenes Weiß als Fortschrittsfüllung.

### Callout-Box
```html
<div class="callout">
  <div class="callout-label">Hinweis</div>
  <div class="callout-text">Inhalt des Hinweises...</div>
</div>
```
CSS: `--bg-2`-Hintergrund, `2px solid --text-dark` linker Rand, Radius 0 8px 8px 0, kursiver Fließtext.

### Metrik-Karte
```html
<div class="metric-card">
  <div class="metric-label">Umsatz</div>
  <div class="metric-val">€ 8.400</div>
  <div class="metric-sub up">↑ 12 % vs. Vorwoche</div>
</div>
```
CSS: weißer Hintergrund, `--border`-Rahmen, `metric-val` bei 24px/600 in `--text-dark`. `.up` = `#3a7d44`, `.down` = `#9b3535`.

## Leitplanken

- Kein Tailwind, kein Bootstrap, keine CSS-Frameworks – nur reines Vanilla-CSS.
- Lucide-Style-Linien-SVGs für Abschnitts-Icons verwenden (klarer als Emojis).
- Keine Verläufe, Glows oder Drop-Shadows – der redaktionelle Stil lebt von flachen Oberflächen und haarfeinen Rahmen.
- Wenn der Nutzer eigene Markenfarben angibt, diese über die Standardwerte stellen.
- Wenn der Nutzer eine Signal-/Akzentfarbe wünscht (z. B. Teal, Blau, Grün), `--accent` ersetzen und Badge-Punkte, Stat-Zahlen, Karten-Tags und Fortschrittsfüllungen konsistent anpassen.
