---
name: architecture-decisions
description: VeloCMS-Architekturentscheidungen die nicht direkt aus dem Code ableitbar sind
metadata: 
  node_type: memory
  type: project
  originSessionId: 793cb0fe-6003-45e0-8f3d-133234777e17
---

# VeloCMS Architecture Decisions

## Kein Laravel/Symfony
Bewusste Entscheidung für ein eigenes MVC-Framework ohne externe Abhängigkeiten.
**Why:** Maximale Kontrolle, minimaler Overhead für KMU-Hosting.

## Multi-Tenancy via Schema-Separation (nicht Row-Level)
Jeder Tenant bekommt eine eigene MySQL-Datenbank, nicht eine Tabelle mit `site_id`.
**Why:** Datenisolation, einfachere Backups pro Kunde, keine Risk of Cross-Tenant-Leaks.
**How to apply:** `velocms_master.velocms_sites` ist die Registry. Site-Resolution via `$_SERVER['HTTP_HOST']`.

## Tenant-ID ist immutable, Domain ist änderbar
Dateipfade und interne Referenzen nutzen `tenant_id` (slug), nie die Domain.
**Why:** Kunden wechseln Domains — interne Daten müssen konsistent bleiben.
**Path-Schema:** `/storage/tenants/{tenant_id}/uploads/`

## JSON-First Visual Editor
Box-Inhalt wird als JSON in `velocms_boxes.data` gespeichert, kein Raw-HTML.
**Why:** Ermöglicht sauberes Re-Rendering, Versionierung, und Mehrsprachigkeit ohne HTML-Parsing.
**Constraint:** Kein Inline-CSS/HTML im JSON. Nur Parameter (spacing, overlay 0-100%, etc.)

## Zwei-Schicht-i18n
- Layer 1: UI-Strings → `lang/de.php` + `lang/en.php` via `t('key')`
- Layer 2: Content → `_en`-Spalten in DB, Auto-Translation via DeepL → Anthropic-Fallback
**Why:** Klare Trennung zwischen CMS-Interface-Sprache und Site-Inhalts-Sprache.

## DSGVO-First
- Keine externen Assets im Frontend (kein Google Fonts, kein CDN)
- Video-Embeds nur 2-Click (Vanilla JS)
- EXIF-Strip vor jedem Bild-Save (Pflicht)
- Kontaktformular-Daten: Cron-Löschung nach 90 Tagen
**Why:** Zielmarkt Deutschland — DSGVO-Compliance ist Verkaufsargument.

## Deploy: GitHub Actions → SSH
Push to `main` → GitHub Actions → SSH auf Hetzner → `git pull + composer + migrate`
**Why:** Operator arbeitet auf Windows, kein direktes rsync/SFTP-Deployment.
