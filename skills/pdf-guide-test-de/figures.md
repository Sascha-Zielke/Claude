# Wiederverwendbare SVG-Grafiken

Drei Referenz-Infografiken, die du kopieren, anpassen und in einen `<figure class="figure">...<figcaption>ABB. NN — Beschriftung.</figcaption></figure>`-Block einfügen kannst.

Palette (ausschließlich diese verwenden):
- `#ffffff` weißer Hintergrund
- `#1a1a1a` fast-schwarze Umrisse und Flächen
- `#b0b0b0` hellgrauer Akzent
- `#f5f5f5` cremeweiße Flächen
- `#7a7a7a` mittelgrau (für Bildunterschriften, per CSS gesteuert)

Alle drei sind auf einer viewBox gezeichnet, die breit genug ist (~600), damit die CSS-Regel `.figure svg { max-width: 5.8in }` sie komfortabel auf der Seite hält.

---

## ABB. 01 — Zwei Ansichten, ein Ordner

Zeigt zwei App-Fenster mit orangefarbenen Pfeilen, die in einen gemeinsamen Ordner fließen. Vermittelt die Kernidee, dass beide Tools auf denselben Ort auf der Festplatte zeigen.

Einsatz: Wenn Integrationen, gemeinsame Datenquellen oder "gleiche Dateien, zwei Ansichten"-Konzepte erklärt werden.

```html
<figure class="figure">
  <svg viewBox="0 0 600 340" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#d97757"/>
      </marker>
    </defs>

    <!-- Linkes App-Fenster -->
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

    <!-- Rechtes App-Fenster -->
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
  <figcaption>ABB. 01 — Beide Apps zeigen auf denselben Ordner auf der Festplatte.</figcaption>
</figure>
```

---

## ABB. 02 — Wissensgraph / Neuronennetz

Ein zentraler orangefarbener Knoten, umgeben von beschrifteten Satelliten-Knoten, verbunden durch dünne schwarze Synapsenlinien. Vermittelt die Idee "deine Notizen bilden ein Netzwerk."

Einsatz: Wenn Second Brains, Wissensgraphen, Konzeptvernetzung oder "eine zentrale Sache verbindet sich mit vielen anderen"-Metaphern erklärt werden.

```html
<figure class="figure">
  <svg viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg">
    <!-- Synapsen zuerst, damit Knoten darüber liegen -->
    <g stroke="#141413" stroke-width="0.7" fill="none" opacity="0.55">
      <line x1="300" y1="160" x2="130" y2="80"/>
      <line x1="300" y1="160" x2="470" y2="80"/>
      <line x1="300" y1="160" x2="90" y2="200"/>
      <line x1="300" y1="160" x2="510" y2="200"/>
      <line x1="300" y1="160" x2="200" y2="270"/>
      <line x1="300" y1="160" x2="400" y2="270"/>
      <line x1="130" y1="80" x2="470" y2="80"/>
      <line x1="90" y1="200" x2="200" y2="270"/>
      <line x1="510" y1="200" x2="400" y2="270"/>
    </g>

    <!-- Zentrum -->
    <g>
      <circle cx="300" cy="160" r="32" fill="#d97757" stroke="#141413" stroke-width="1.5"/>
      <text x="300" y="164" text-anchor="middle" font-family="Poppins,Arial" font-size="9" font-weight="600" fill="#faf9f5">ZENTRUM</text>
    </g>

    <!-- Satelliten (Labels nach Bedarf umbenennen) -->
    <g font-family="Lora,Georgia" font-size="9" fill="#141413">
      <circle cx="130" cy="80" r="8" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="130" y="65" text-anchor="middle" font-style="italic">Label A</text>

      <circle cx="470" cy="80" r="8" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="470" y="65" text-anchor="middle" font-style="italic">Label B</text>

      <circle cx="90" cy="200" r="8" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="90" y="220" text-anchor="middle" font-style="italic">Label C</text>

      <circle cx="510" cy="200" r="8" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="510" y="220" text-anchor="middle" font-style="italic">Label D</text>

      <circle cx="200" cy="270" r="8" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="200" y="290" text-anchor="middle" font-style="italic">Label E</text>

      <circle cx="400" cy="270" r="8" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="400" y="290" text-anchor="middle" font-style="italic">Label F</text>
    </g>
  </svg>
  <figcaption>ABB. 02 — Eine zentrale Idee, verbunden mit allem um sie herum.</figcaption>
</figure>
```

---

## ABB. 03 — Eingabe-Pillen → zentraler Prozessor → Ausgabe-Karte

Zeigt Quell-Pillen links, die in einen zentralen dunklen Kreis fließen (ein Prozess, ein Zeitplan, ein Agent) und heraus zu einer gestalteten Karte rechts.

Einsatz: Wenn ein Workflow, eine geplante Aufgabe, eine Pipeline oder "viele Dinge gehen rein, eines kommt heraus"-Abläufe erklärt werden.

```html
<figure class="figure">
  <svg viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#d97757"/>
      </marker>
    </defs>

    <!-- Quell-Pillen (frei umbenennen) -->
    <g font-family="Poppins,Arial" font-size="10" font-weight="600">
      <rect x="30" y="40" width="120" height="34" rx="17" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="90" y="61" text-anchor="middle" fill="#141413">Quelle A</text>

      <rect x="30" y="122" width="120" height="34" rx="17" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="90" y="143" text-anchor="middle" fill="#141413">Quelle B</text>

      <rect x="30" y="204" width="120" height="34" rx="17" fill="#faf9f5" stroke="#141413" stroke-width="1.2"/>
      <text x="90" y="225" text-anchor="middle" fill="#141413">Quelle C</text>
    </g>

    <g stroke="#d97757" stroke-width="1.5" fill="none">
      <path d="M 150 57 Q 220 57 260 120" marker-end="url(#arrow2)"/>
      <path d="M 150 139 L 260 139" marker-end="url(#arrow2)"/>
      <path d="M 150 221 Q 220 221 260 158" marker-end="url(#arrow2)"/>
    </g>

    <!-- Zentraler Prozessor -->
    <g>
      <circle cx="320" cy="140" r="58" fill="#141413" stroke="#d97757" stroke-width="2"/>
      <text x="320" y="130" text-anchor="middle" font-family="Poppins,Arial" font-size="11" font-weight="600" fill="#faf9f5">PROZESS</text>
      <text x="320" y="148" text-anchor="middle" font-family="Lora,Georgia" font-size="9" font-style="italic" fill="#d97757">läuft nach Zeitplan</text>
      <text x="320" y="165" text-anchor="middle" font-family="Poppins,Arial" font-size="13" font-weight="600" fill="#faf9f5">18:00 Uhr</text>
    </g>

    <g stroke="#d97757" stroke-width="1.5" fill="none">
      <path d="M 378 140 L 440 140" marker-end="url(#arrow2)"/>
    </g>

    <!-- Ausgabe-Karte -->
    <g>
      <rect x="450" y="75" width="130" height="130" rx="4" fill="#e8e6dc" stroke="#141413" stroke-width="1.2"/>
      <rect x="450" y="75" width="130" height="20" rx="4" fill="#141413"/>
      <text x="515" y="89" text-anchor="middle" font-family="Poppins,Arial" font-size="8" font-weight="600" fill="#faf9f5">AUSGABE</text>
      <line x1="462" y1="110" x2="568" y2="110" stroke="#141413" stroke-width="0.6"/>
      <line x1="462" y1="122" x2="555" y2="122" stroke="#141413" stroke-width="0.6"/>
      <line x1="462" y1="134" x2="568" y2="134" stroke="#141413" stroke-width="0.6"/>
      <line x1="462" y1="146" x2="540" y2="146" stroke="#141413" stroke-width="0.6"/>
      <line x1="462" y1="158" x2="568" y2="158" stroke="#141413" stroke-width="0.6"/>
      <line x1="462" y1="170" x2="530" y2="170" stroke="#141413" stroke-width="0.6"/>
      <text x="515" y="200" text-anchor="middle" font-family="Lora,Georgia" font-size="8" font-style="italic" fill="#141413">wartet auf dich</text>
    </g>
  </svg>
  <figcaption>ABB. 03 — Quellen fließen hinein, ein poliertes Ergebnis kommt heraus.</figcaption>
</figure>
```

---

## Tipps für neue Grafiken

- Mit der nächstliegenden der drei Vorlagen beginnen und Labels umbenennen. Nie von Null.
- Die gesamte Grafikhöhe in der viewBox unter ~340 halten, damit sie nie eine Seite dominiert.
- Text in SVGs umbricht nicht; Labels kurz halten und nicht auf sie als Hauptinformationsträger verlassen. Die Bildunterschrift ist der Ort für die vollständige Aussage.
- Wenn mehr als ~8 beschriftete Elemente nötig sind, ist die Grafik zu voll. Aufteilen oder vereinfachen.
