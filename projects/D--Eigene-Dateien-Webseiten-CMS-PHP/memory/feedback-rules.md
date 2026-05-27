---
name: feedback-rules
description: "Verhaltensregeln für Claude Code bei veloCMS — Autonomie, Command-Format, Session-Protokoll"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 793cb0fe-6003-45e0-8f3d-133234777e17
---

# Behavioral Rules for veloCMS Development

## Autonomie-Modus
Immer mit maximaler Autonomie arbeiten. `--permission-mode auto` annehmen.
Pre-approved: `ssh`, `scp`, `git`, `composer`, `npm`, `php velocms *`.

**Why:** Operator führt mehrere parallele Sessions und will keine Approval-Loops.
**How to apply:** Direkt ausführen ohne Bestätigungs-Rückfrage, außer bei destruktiven DB-Operationen.

## Command-Format (ABSOLUT)
Jeden ausführbaren Befehl in einem eigenen Markdown-Codeblock. Niemals Commands inline im Fließtext oder aufgeteilt auf mehrere Blöcke.

**Why:** Operator muss Commands mit einem Klick kopieren können.
**How to apply:** Auch für kurze Commands wie `nginx -t` einen eigenen Codeblock verwenden.

## Session-Protokoll (MANDATORY)
1. Session-Start: RESUME.md lesen
2. Session-Ende: RESUME.md + SESSION_LOG.md aktualisieren
3. Dann: `git add -A && git commit && git push`
4. `/clear` zwischen Major-Phases

**Why:** Mehrere parallele Sessions — Zustandssynchronisation über RESUME.md.

## Double-Audit Gate (PFLICHT — kein Opt-out)
Niemals eine Phase starten bevor die aktuelle Phase BEIDE Audits bestanden hat.
- **Audit 1:** Trockener Code-Review gegen Architektur-Constraints (Sicherheit, Style, Namespaces, Migrations)
- **Audit 2:** Live-Verify auf dem Server — mind. 3 curl-Commands gegen die echte Domain

**Explizite Nutzer-Anweisung (2026-05-26):** "Nach jeder Phase führst du das geforderte Audit durch. Merke dir das."
**Why:** Fehler in frühen Phasen kaskadieren in allen späteren. Audit-Lücken wurden Session 5 beanstandet.
**How to apply:** Audit 1 + 2 sofort nach Commit — vor git push wenn möglich, sonst direkt nach Deploy.

## Design-Verbote
- Keine Neon-Gradienten oder Tech-Glow-Ästhetik
- Keine externen CDN-Calls (Fonts, Icons, Scripts)
- Keine absoluten URLs in der Datenbank
- Kein Inline-HTML/CSS im JSON der Visual-Editor-Boxes

## PHP-Regeln
- `declare(strict_types=1)` in jeder PHP-Datei
- Alle DB-Queries via PDO Prepared Statements
- Alle HTML-Ausgaben via `e()` helper
- CSRF-Check (`Auth::verifyCsrf()`) als erste Zeile jedes POST-Handlers
