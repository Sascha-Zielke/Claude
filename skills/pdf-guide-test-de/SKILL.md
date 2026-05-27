---
name: pdf-guide-test
description: Verwandelt jeden geschriebenen Leitfaden, jede Checkliste, jedes Playbook, jede Schritt-für-Schritt-Anleitung oder jedes Tutorial in ein poliertes PDF im redaktionellen Magazinstil. Kommt mit einem sauberen, professionellen hellen Editorial-Look (cremefarbener Hintergrund, schwarzer Text, hellgraue Akzente, Poppins + Lora Schriften, nummerierte Schritte, Copy-Paste-Promptblöcke, Callouts, inline SVG-Grafiken), der mit eigenen Markenfarben, Schriften oder Tonalität überschrieben werden kann. Auslöser-Phrasen: "erstell einen Leitfaden", "schreib einen Guide", "bau mir eine Anleitung", "mach eine Checkliste", "wandle das in einen Guide um", "Cheatsheet für", "Walkthrough zu", "Setup-Anleitung für", "How-to zu", "Playbook für", "Tutorial zu", "schreib das auf", "mach eine Ressource daraus". Nur überspringen bei kurzen Posts, Slide Decks oder wenn der User explizit docx oder reines Markdown möchte.
---

# PDF-Leitfaden

Dieser Skill verwandelt einen geschriebenen Leitfaden (Setup-Anleitung, Cheatsheet, Playbook usw.) in ein poliertes PDF mit einem redaktionellen Magazin-Look. Einsetzen, wenn das Ergebnis ein eigenständiges, teilbares Dokument sein soll, das jemand herunterlädt, liest und behält.

## Anpassung an deine Marke

Die Standardwerte unten ergeben direkt einen warmen redaktionellen Look. Jedes Element lässt sich überschreiben, indem du Claude sagst:
- **Farben:** "Benutze meine Markenfarben — Navy #0a2540 und Gold #c6a656"
- **Schriften:** "Verwende Georgia für den Fließtext und Helvetica Bold für Überschriften"
- **Tonalität:** "Schreib es in einem formellen, sachlichen Ton" (überschreibt den lockeren Standard)
- **Cover-Stil:** "Kein Magazin-Cover, fang direkt mit dem Inhalt an"

Wenn keine Angaben gemacht werden, gelten die Standardwerte.

## Standard-Ausgabe-Look

Ein DIN-A4- oder Letter-PDF mit:

- **Titelseite**: cremefarbener Hintergrund (#f8f7f3), schwarze Wortmarken-Linie und Text, großer schwarzer Poppins-Display-Titel, hellgrauer Akzentbalken, kursiver grauer Lora-Untertitel, dreispaltiger Byline-Bereich unten (Verfasst von / Veröffentlicht / Community oder ähnlich). Klar, minimal, professionell.
- **Inhaltsseiten**: weißer Hintergrund, schwarzer Fließtext (#1a1a1a), unterstrichene Poppins-Abschnittsüberschriften in Schwarz, hellgraue (#b0b0b0) Akzente, Fußzeile in Mittelgrau (#7a7a7a).
- **Callout-Box**: cremefarbener (#f5f5f5) Hintergrund, schwarzer linker Rand, kleines schwarzes Label in Großbuchstaben.
- **Nummerierte Schritte**: große schwarze Poppins-Ziffern neben Poppins-Titeln und schwarzem Lora-Fließtext, getrennt durch dünne graue Linien. Keine Kreis-Hintergründe.
- **Prompt-Blöcke**: dunkelgrauer Hintergrund (#2d2d2d), weißer kursiver Lora-Text, hellgraues Label in Großbuchstaben, hellgrauer linker Rand. Zum Kopieren und Einfügen gedacht.
- **Tools-Abschnitt**: haarliniengetrennte Zeilen mit Tool-Name in Poppins, kursive graue Meta-Zeile, schwarze Lora-Beschreibung.
- **Checkliste**: nullaufgefüllte Dezimalzahlen (01, 02, 03) in Schwarz, Haarlinienzeilen.
- **Schlusszeile**: kursives "Bis bald," (oder ähnlich) über einem Poppins-Display-Namen.
- **Inline SVG-Grafiken** (optional, aber empfohlen): in derselben Farbpalette gezeichnet mit kursiven "ABB. NN"-Beschriftungen in Hellgrau.

## So erstellst du einen neuen Leitfaden

Der Skill enthält ein Python-Vorlagen-Script (`build_guide_pdf.py`) und eine wiederverwendbare Grafik-Bibliothek (`figures.md`), die WeasyPrint verwenden. Ablauf:

1. **Vorlage kopieren** in dein Arbeitsverzeichnis. Nie die Skill-Kopie direkt bearbeiten.
   - Benutze `build_guide_pdf.py` als Basis. Ändere `OUT = "dein-leitfaden-titel.pdf"` auf deinen Ziel-Dateinamen.
2. **Inhalte befüllen**: Cover-Felder (Eyebrow, Titel, Untertitel, Byline-Werte, Dokumentnummer), dann den HTML-Body (Abschnitte, Callouts, Schritte, Prompts, Tools, Checkliste, Schlusszeile).
3. **Palette/Schriften tauschen** am Anfang des Scripts, wenn der User Marken-Overrides angegeben hat.
4. **Grafiken dort einsetzen, wo sie etwas lehren**, das Text allein nicht kann. Nicht zur Dekoration, sondern zur Illustration. Gute Auslöser: eine Beziehung zwischen zwei Dingen, ein Ablauf über Zeit, ein Konzept, das von einer Metapher profitiert. Wenn eine Grafik ihren Platz nicht verdient, weglassen.
   - `figures.md` enthält drei produktionsreife SVG-Vorlagen:
     - **ABB. 01** (Zwei Ansichten, ein Ordner): Zwei App-Fenster mit Pfeilen, die in einen gemeinsamen Ordner fließen. Für Integrationen, gemeinsame Datenquellen, "gleiche Dateien, zwei Ansichten"-Konzepte.
     - **ABB. 02** (Wissensgraph): Zentraler orangefarbener Knoten, umgeben von beschrifteten Satelliten, verbunden durch dünne Synapsenleitungen. Für Second Brains, Wissensgraphen, Konzeptvernetzung.
     - **ABB. 03** (Eingabe → Verarbeitung → Ausgabe): Quell-Pillen fließen in einen zentralen dunklen Prozessor und heraus zu einer gestalteten Ausgabe-Karte. Für Workflows, geplante Aufgaben, Pipelines, "viele hinein, eines heraus"-Abläufe.
   - Kopieren, Labels umbenennen, Farben anpassen. Nie von Null anfangen.
5. **OUT-Pfad setzen** am Anfang des Scripts auf die gewünschte Ausgabedatei.
6. **Script ausführen**: `python build_guide_pdf.py`
7. **Vorschau prüfen** mit `pdftoppm -png -r 90 <pdf> prev`, dann die PNGs öffnen und das Layout prüfen. Cover, mindestens eine Grafikseite und mindestens eine Inhaltsseite checken.

Die Vorlage ist vollständig eigenständig. Die einzige Systemabhängigkeit ist WeasyPrint (`pip install weasyprint`).

## Standard-Designentscheidungen

Diese lassen das Ergebnis wie ein sauberes, professionelles Redaktionsstück wirken. Beibehalten, sofern der User keine Änderungen wünscht.

- **Standard-Palette**: `#f8f7f3` Cremeweiß-Hintergrund, `#1a1a1a` Schwarz, `#b0b0b0` Hellgrau (Akzente), `#7a7a7a` Mittelgrau (Meta-Text, Fußzeilen). Tauschen, wenn der User Markenfarben angegeben hat.
- **Standard-Typografie**: Poppins (600) für Display/Überschriften/Labels, Lora für den gesamten Fließtext und alle kursiven Elemente. Georgia/Arial als Fallbacks. Tauschen, wenn gewünscht.
- **Haarlinien statt Boxen**: Abschnittsüberschriften bekommen eine einzelne 0,75pt-Unterlinie, Schrittzeilen und Checklistenpunkte nutzen 0,5pt-Trennlinien. Keine dicken Rundeck-Container; sie lassen es wie ein Template aussehen.
- **Klarer Kontrast**: Schwarzer Text auf weißem/cremefarbenem Hintergrund ist der Standard. Hellgrau ist nur für unterstützende Texte und Akzente — nie für primären Inhalt.
- **Prompt-Blöcke sind dunkel auf hell**: Der dunkle Hintergrund markiert Copy-Paste-Inhalte, ohne zu hart zu wirken. Gute Lesbarkeit.
- **Großzügiger Weißraum**: 0,95in Seitenränder, 30pt Abstand über h2, 22pt um Grafiken. Die Seite soll atmen.

## Standard-Tonalität im Leitfaden

Das PDF soll sich lesen wie ein Freund, der jemanden durch ein Setup führt — kein Unternehmens-Whitepaper. Wenn der User einen formelleren oder technischeren Ton wünscht, umschalten.

- Locker, freundlich, im Erkläre-es-einem-Freund-Stil.
- Kurze Absätze. Klares Deutsch. Kein Fachjargon ohne Erklärung.
- Den Leser direkt ansprechen ("du").
- Wenn Prompts enthalten sind, wörtlich zitieren, damit Leser sie kopieren können.

## Grafik-Richtlinien

Grafiken sind inline SVG innerhalb von `<figure class="figure">` mit einem `<figcaption>ABB. NN &mdash; kurze Beschriftung.</figcaption>`. Drei produktionsreife Referenzvorlagen sind in `figures.md` dokumentiert:

- **ABB. 01 — Zwei Ansichten, ein Ordner**: Zwei App-Fenster mit grauen Pfeilen, die in einen gemeinsamen Ordner fließen. Vermittelt: Beide Tools zeigen auf denselben Ort auf der Festplatte.
- **ABB. 02 — Wissensgraph / Neuronennetz**: Zentraler hellgrauer Knoten, umgeben von beschrifteten Satelliten, verbunden durch dünne schwarze Synapsenlinien. Vermittelt: Notizen bilden ein Netzwerk, Konzepte vernetzen sich.
- **ABB. 03 — Eingabe-Pillen → Verarbeitung → Ausgabe-Karte**: Quell-Pillen links fließen in einen zentralen dunklen Kreis (ein Prozess, ein Zeitplan, ein Agent) und heraus zu einer gestalteten Karte rechts. Vermittelt: Pipelines und "viele hinein, eines heraus"-Abläufe.

Beim Erstellen neuer Grafiken:

- Die aktive Palette verwenden (Standardwerte oder Markenfarben des Users).
- Mit der nächstliegenden der drei Vorlagen beginnen und Labels umbenennen. Nie von Null.
- Dünne Striche (1 bis 1,5pt). Umrisse bevorzugen statt Flächen, außer für Betonungsknoten.
- ViewBoxes ca. 600 breit. Das CSS begrenzt die gerenderte Breite auf 5,8in.
- Alles beschriften: Display-Schrift für UI/Labels, kursive Serifenschrift für Randnotizen.
- Beschriftungen beginnen mit `ABB. NN &mdash;`, die Hauptaussage steht in der Beschriftung, da SVG-Text nicht umbricht.
- Wenn mehr als ~8 beschriftete Elemente nötig sind, ist die Grafik zu voll. Aufteilen oder vereinfachen.

## Wann dieser Skill NICHT eingesetzt werden sollte

- Kurze Posts, Ankündigungen und Social-Media-Inhalte. Die bleiben als Markdown.
- Slide Decks. Dafür einen Präsentations-Skill verwenden.
- Interne Notizen oder Entwürfe. PDF ist für polierte, teilbare Endergebnisse.
- Alles, was der User danach selbst bearbeiten möchte. PDFs sind schwer editierbar; stattdessen eine docx- oder Markdown-Version anbieten.

## Ausgabe

Das fertige PDF in den Arbeits-/Ausgabeordner des Users schreiben, mit einem beschreibenden Kebab-Case-Dateinamen (z. B. `dein-leitfaden-titel.pdf`), dann als Link zurückgeben, damit es mit einem Klick geöffnet oder angehängt werden kann.
