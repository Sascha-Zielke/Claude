# Redaktionelles PDF-Leitfaden-Template.
#
# So erstellst du einen neuen Leitfaden:
#   1. Diese Datei in dein Arbeitsverzeichnis kopieren (nicht die Skill-Kopie bearbeiten).
#   2. OUT auf deinen gewünschten PDF-Pfad ändern.
#   3. Die Cover-Felder befüllen (Wortmarke, Eyebrow, h1, Untertitel, Byline-Werte).
#   4. Die Abschnitte im Body durch deinen Leitfaden-Inhalt ersetzen.
#   5. Grafiken hinzufügen oder entfernen. Sieh figures.md für wiederverwendbare SVGs.
#   6. Ausführen: python build_guide_pdf.py
#
# Designregeln stehen in SKILL.md. Kurzversion:
#   Palette = Cremeweiß #f8f7f3, Schwarz #1a1a1a, Hellgrau #b0b0b0, Mittelgrau #7a7a7a
#   Poppins für Display/Überschriften, Lora für Fließtext.
#   Hellgrau ist ein Akzent, keine Fläche.
#
# Benötigt: pip install weasyprint

from weasyprint import HTML, CSS

# Hier den Ziel-PDF-Ausgabepfad eintragen.
OUT = "dein-leitfaden-titel.pdf"

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Dein Leitfaden-Titel</title>
</head>
<body>

<!-- =========================================================
     TITELSEITE
     Wortmarke, Eyebrow, Titel, Untertitel und Byline anpassen.
     ========================================================= -->
<section class="cover">
  <div class="cover-top">
    <div class="wordmark">Deine Marke oder dein Projekt</div>
    <div class="doc-type">Leitfaden &middot; Nr. 01</div>
  </div>

  <div class="cover-middle">
    <div class="eyebrow">Eine kurze, kursive Tagline</div>
    <h1>Der Leitfaden-<br>Titel</h1>
    <div class="rule"></div>
    <div class="subtitle">Ein oder zwei Sätze Untertitel, der dem Leser genau sagt, was er mitnimmt. Konkret und spezifisch halten.</div>
  </div>

  <div class="cover-bottom">
    <div class="byline-col">
      <div class="byline-label">Verfasst von</div>
      <div class="byline-value">Name des Autors</div>
    </div>
    <div class="byline-col">
      <div class="byline-label">Veröffentlicht</div>
      <div class="byline-value">Monat Jahr</div>
    </div>
    <div class="byline-col">
      <div class="byline-label">Community</div>
      <div class="byline-value">dein-link.com</div>
    </div>
  </div>
</section>

<!-- =========================================================
     INHALT
     Hier lebt der Leitfaden-Body. Die folgenden Abschnitte
     zeigen jede Komponente, die das Stylesheet unterstützt:
       - h2 Abschnittsüberschriften
       - Absätze + Fettschrift
       - Callout-Box
       - Grafiken (inline SVG)
       - Nummerierte Schritte
       - Prompt-Blöcke (zum Kopieren)
       - Tools-Abschnitt
       - Checkliste
       - Schlusszeile

     Beispielinhalte löschen, Komponenten-Markup behalten.
     ========================================================= -->
<section class="content">

<h2>Abschnitt Eins: Das Problem</h2>
<p>Mit dem Schmerzpunkt beginnen, den dieser Leitfaden löst. Kurz und konkret halten. Der Leser soll sich im ersten Absatz wiedererkennen und denken: "Ja, genau das ist mein Problem."</p>

<p>Danach ein Satz Versprechen, was dieser Leitfaden für ihn tut. Zum Beispiel: Am Ende dieses Leitfadens hast du <b>das, was der Leser möchte</b> in unter fünfzehn Minuten zum Laufen gebracht.</p>

<div class="callout">
  <div class="callout-title">Die zentrale Idee</div>
  <div class="callout-body">Callouts dienen dazu, den Kerngedanken eines Abschnitts in ein oder zwei Sätzen zusammenzufassen. Sie unterbrechen lange Textpassagen und geben dem Leser einen Moment zum Ankommen.</div>
</div>

<figure class="figure">
  <svg viewBox="0 0 600 340" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#d97757"/>
      </marker>
    </defs>

    <!-- Linkes Fenster -->
    <g>
      <rect x="40" y="40" width="200" height="120" rx="6" fill="#faf9f5" stroke="#141413" stroke-width="1.5"/>
      <rect x="40" y="40" width="200" height="22" rx="6" fill="#141413"/>
      <circle cx="52" cy="51" r="3" fill="#d97757"/>
      <circle cx="62" cy="51" r="3" fill="#faf9f5"/>
      <circle cx="72" cy="51" r="3" fill="#faf9f5"/>
      <text x="140" y="55" text-anchor="middle" font-family="Poppins,Arial" font-size="10" font-weight="600" fill="#faf9f5">APP EINS</text>
      <line x1="60" y1="85" x2="220" y2="85" stroke="#e8e6dc" stroke-width="1.5"/>
      <line x1="60" y1="100" x2="200" y2="100" stroke="#e8e6dc" stroke-width="1.5"/>
      <line x1="60" y1="115" x2="210" y2="115" stroke="#e8e6dc" stroke-width="1.5"/>
      <line x1="60" y1="130" x2="180" y2="130" stroke="#e8e6dc" stroke-width="1.5"/>
    </g>

    <!-- Rechtes Fenster -->
    <g>
      <rect x="360" y="40" width="200" height="120" rx="6" fill="#faf9f5" stroke="#141413" stroke-width="1.5"/>
      <rect x="360" y="40" width="200" height="22" rx="6" fill="#141413"/>
      <circle cx="372" cy="51" r="3" fill="#d97757"/>
      <circle cx="382" cy="51" r="3" fill="#faf9f5"/>
      <circle cx="392" cy="51" r="3" fill="#faf9f5"/>
      <text x="460" y="55" text-anchor="middle" font-family="Poppins,Arial" font-size="10" font-weight="600" fill="#faf9f5">APP ZWEI</text>
    </g>

    <!-- Pfeile nach unten -->
    <g stroke="#d97757" stroke-width="1.5" fill="none">
      <path d="M 140 170 L 140 210 L 260 210 L 260 240" marker-end="url(#arrow)"/>
      <path d="M 460 170 L 460 210 L 340 210 L 340 240" marker-end="url(#arrow)"/>
    </g>

    <!-- Gemeinsamer Ordner -->
    <g>
      <path d="M 220 250 L 260 250 L 275 264 L 380 264 L 380 312 L 220 312 Z" fill="#e8e6dc" stroke="#141413" stroke-width="1.5"/>
      <text x="300" y="292" text-anchor="middle" font-family="Poppins,Arial" font-size="11" font-weight="600" fill="#141413">Gemeinsamer Ordner</text>
      <text x="300" y="305" text-anchor="middle" font-family="Lora,Georgia" font-size="8" font-style="italic" fill="#141413">ein Ort, zwei Ansichten</text>
    </g>
  </svg>
  <figcaption>ABB. 01 &mdash; Eine kurze Beschriftung, die erklärt, was die Grafik zeigt.</figcaption>
</figure>

<h2>Abschnitt Zwei: Das Setup</h2>
<p>Diesen Abschnitt nutzen, um den Leser durch das Setup zu führen. Nummerierte Schritte funktionieren am besten. Jeden Schritt auf einen Satz Anweisung plus ein oder zwei Sätze Erklärung beschränken.</p>

<div class="step">
  <div class="step-num">1</div>
  <div class="step-content">
    <div class="step-title">Das erste, was zu tun ist</div>
    <div class="step-body">Eine Ein-Satz-Anweisung. Dann kurz erklären, warum dieser Schritt wichtig ist.</div>
  </div>
</div>

<div class="step">
  <div class="step-num">2</div>
  <div class="step-content">
    <div class="step-title">Das nächste, was zu tun ist</div>
    <div class="step-body">Die Anweisungen knapp halten. Davon ausgehen, dass der Leser klug ist, aber neu in diesem Thema.</div>
  </div>
</div>

<div class="step">
  <div class="step-num">3</div>
  <div class="step-content">
    <div class="step-title">Das dritte, was zu tun ist</div>
    <div class="step-body">Wenn ein Schritt einen Prompt hat, direkt danach einfügen. Siehe unten.</div>
  </div>
</div>

<div class="prompt">
  <div class="prompt-label">PROMPT 1 / KURZE BESCHREIBUNG</div>
  <div class="prompt-body">Prompt-Blöcke sind für Inhalte gedacht, die der Leser kopieren und einfügen soll. Der dunkle Hintergrund signalisiert "das ist etwas zum Mitnehmen." Prompts in klarer Sprache schreiben, in der ersten Person, wenn es zum Ton des Leitfadens passt.</div>
</div>

<div class="step">
  <div class="step-num">4</div>
  <div class="step-content">
    <div class="step-title">Das letzte, was zu tun ist</div>
    <div class="step-body">Das Setup-Kapitel so abschließen, dass der Leser das Gefühl hat, etwas Echtes abgeschlossen zu haben.</div>
  </div>
</div>

<h2>Abschnitt Drei: Warum das funktioniert</h2>
<p>Nach dem Setup den Mehrwert erklären. Was hat der Leser jetzt, was er vorher nicht hatte? Was kann er damit anfangen? Den Ton zuversichtlich und konkret halten.</p>

<p>Hier ist auch ein guter Platz für eine zweite Grafik, wenn der Mehrwert von einer Visualisierung profitiert. Sieh figures.md für drei Referenz-SVGs zum Anpassen.</p>

<h2>Tools, die du brauchst</h2>
<div class="tools">
  <div class="tool">
    <div class="tool-name">Tool Eins</div>
    <div class="tool-meta">Kostenlos / tool-eins.com</div>
    <div class="tool-desc">Ein Satz darüber, was das Tool tut und warum es für dieses Setup wichtig ist.</div>
  </div>
  <div class="tool">
    <div class="tool-name">Tool Zwei</div>
    <div class="tool-meta">Kostenlos oder kostenpflichtig / tool-zwei.com</div>
    <div class="tool-desc">Tool-Beschreibungen kurz halten. Der Leser kann selbst nachklicken, wenn er mehr will.</div>
  </div>
</div>

<h2>Das kannst du heute noch tun</h2>
<p>Mit einer kurzen Aktions-Checkliste abschließen. Drei konkrete Dinge wählen, die der Leser in den nächsten fünfzehn Minuten tun kann. Nicht zehn. Drei ist der Sweet Spot.</p>
<ol class="checklist">
  <li>Die kleinste mögliche erste Aktion.</li>
  <li>Die Aktion, die einen auf halbem Weg bringt.</li>
  <li>Die Aktion, die es abschließt.</li>
</ol>
<p>Wer diese drei Dinge tut, hat bereits den größten Teil des Nutzens aus diesem Leitfaden gezogen.</p>

<div class="signoff">
  <div class="signoff-text">Bis bald,</div>
  <div class="signoff-name">Autor</div>
</div>

</section>

</body>
</html>
"""

css = """
@page {
  size: Letter;
  margin: 0.95in 0.95in 1.1in 0.95in;
  background: #ffffff;
  @bottom-center {
    content: "Dein Leitfaden-Titel   \\2022   Name des Autors   \\2022   " counter(page);
    font-family: 'Lora', 'Georgia', serif;
    font-size: 9pt;
    color: #7a7a7a;
  }
}

@page :first {
  margin: 0;
  @bottom-center { content: ""; }
}

* { box-sizing: border-box; }

html, body { background: #ffffff; }

body {
  font-family: 'Lora', 'Georgia', serif;
  color: #1a1a1a;
  font-size: 11pt;
  line-height: 1.65;
  margin: 0;
  padding: 0;
}

/* COVER */
.cover {
  page: cover;
  width: 8.5in;
  height: 11in;
  background: #f8f7f3;
  color: #1a1a1a;
  position: relative;
  page-break-after: always;
  padding: 0.95in 0.95in 0.95in 0.95in;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.cover-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 0.75pt solid #1a1a1a;
  padding-bottom: 14pt;
}
.wordmark {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 10pt;
  font-weight: 600;
  letter-spacing: 0.5pt;
  color: #1a1a1a;
}
.doc-type {
  font-family: 'Lora', 'Georgia', serif;
  font-style: italic;
  font-size: 10pt;
  color: #1a1a1a;
}

.cover-middle {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 6.2in;
}
.eyebrow {
  font-family: 'Lora', 'Georgia', serif;
  font-style: italic;
  font-size: 13pt;
  color: #7a7a7a;
  margin-bottom: 18pt;
}
.cover h1 {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 76pt;
  line-height: 0.95;
  font-weight: 600;
  margin: 0 0 26pt 0;
  letter-spacing: -2pt;
  color: #1a1a1a;
}
.rule {
  width: 0.6in;
  height: 3pt;
  background: #b0b0b0;
  margin: 0 0 22pt 0;
}
.subtitle {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 14pt;
  line-height: 1.55;
  color: #1a1a1a;
  max-width: 5.5in;
  font-weight: 400;
}

.cover-bottom {
  display: flex;
  justify-content: flex-start;
  gap: 0.55in;
  border-top: 0.75pt solid #1a1a1a;
  padding-top: 14pt;
}
.byline-col { min-width: 1.6in; }
.byline-label {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 8pt;
  letter-spacing: 1pt;
  text-transform: uppercase;
  color: #7a7a7a;
  margin-bottom: 3pt;
}
.byline-value {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 11pt;
  color: #1a1a1a;
}

/* INHALT */
.content { padding-top: 0.1in; }

h2 {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 20pt;
  font-weight: 600;
  color: #1a1a1a;
  margin: 30pt 0 12pt 0;
  padding-bottom: 8pt;
  border-bottom: 0.75pt solid #1a1a1a;
  letter-spacing: -0.5pt;
}

p {
  margin: 0 0 11pt 0;
  font-family: 'Lora', 'Georgia', serif;
  color: #1a1a1a;
}

b, strong { color: #1a1a1a; font-weight: 700; }

/* CALLOUT */
.callout {
  background: #f5f5f5;
  border-left: 3pt solid #2d2d2d;
  padding: 14pt 18pt;
  margin: 16pt 0;
}
.callout-title {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 8pt;
  font-weight: 600;
  letter-spacing: 1.5pt;
  text-transform: uppercase;
  color: #2d2d2d;
  margin-bottom: 5pt;
}
.callout-body {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 11pt;
  color: #2d2d2d;
  line-height: 1.6;
}

/* SCHRITTE */
.step {
  display: flex;
  align-items: flex-start;
  margin: 0;
  padding: 12pt 0;
  border-bottom: 0.5pt solid #f5f5f5;
}
.step:last-of-type { border-bottom: none; }

.step-num {
  font-family: 'Poppins', 'Arial', sans-serif;
  width: 28pt;
  font-weight: 600;
  font-size: 16pt;
  color: #2d2d2d;
  margin-right: 14pt;
  flex-shrink: 0;
  line-height: 1;
  padding-top: 2pt;
}
.step-content { flex: 1; }
.step-title {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 12pt;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 3pt;
}
.step-body {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 11pt;
  color: #2d2d2d;
  line-height: 1.55;
}

/* PROMPTS */
.prompt {
  background: #2d2d2d;
  color: #ffffff;
  padding: 16pt 20pt;
  margin: 16pt 0;
  border-left: 3pt solid #9a9a9a;
}
.prompt-label {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 8pt;
  font-weight: 600;
  letter-spacing: 2pt;
  color: #9a9a9a;
  margin-bottom: 8pt;
  text-transform: uppercase;
}
.prompt-body {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #ffffff;
  font-style: italic;
}

/* TOOLS */
.tools { margin: 12pt 0; }
.tool {
  border-top: 0.5pt solid #f5f5f5;
  padding: 12pt 0;
}
.tool:last-child { border-bottom: 0.5pt solid #f5f5f5; }
.tool-name {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 13pt;
  font-weight: 600;
  color: #1a1a1a;
}
.tool-meta {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 10pt;
  color: #9a9a9a;
  font-style: italic;
  margin: 2pt 0 4pt 0;
}
.tool-desc {
  font-family: 'Lora', 'Georgia', serif;
  font-size: 11pt;
  color: #2d2d2d;
}

/* CHECKLISTE */
.checklist {
  padding-left: 0;
  list-style: none;
  counter-reset: item;
  margin: 12pt 0;
}
.checklist li {
  counter-increment: item;
  padding: 10pt 0 10pt 36pt;
  position: relative;
  font-family: 'Lora', 'Georgia', serif;
  font-size: 11pt;
  border-bottom: 0.5pt solid #f5f5f5;
  color: #2d2d2d;
}
.checklist li:first-child { border-top: 0.5pt solid #f5f5f5; }
.checklist li::before {
  content: counter(item, decimal-leading-zero);
  position: absolute;
  left: 0;
  top: 10pt;
  font-family: 'Poppins', 'Arial', sans-serif;
  color: #2d2d2d;
  font-weight: 600;
  font-size: 11pt;
}

/* SCHLUSSZEILE */
.signoff {
  margin-top: 28pt;
  padding-top: 18pt;
  border-top: 0.75pt solid #1a1a1a;
}
.signoff-text {
  font-family: 'Lora', 'Georgia', serif;
  font-style: italic;
  font-size: 12pt;
  color: #2d2d2d;
}
.signoff-name {
  font-family: 'Poppins', 'Arial', sans-serif;
  font-size: 16pt;
  font-weight: 600;
  color: #1a1a1a;
  margin-top: 4pt;
}

.pagebreak { page-break-after: always; }

/* GRAFIKEN */
.figure {
  margin: 22pt 0;
  padding: 14pt 0 0 0;
  text-align: center;
  page-break-inside: avoid;
}
.figure svg {
  width: 100%;
  max-width: 5.8in;
  height: auto;
}
.figure figcaption {
  font-family: 'Lora', 'Georgia', serif;
  font-style: italic;
  font-size: 9pt;
  color: #9a9a9a;
  margin-top: 10pt;
  letter-spacing: 0.2pt;
}
"""

HTML(string=html).write_pdf(OUT, stylesheets=[CSS(string=css)])
print(f"Gespeichert: {OUT}")
