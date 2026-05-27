---
name: project-velocms
description: VeloCMS - modular PHP CMS being built from scratch with Claude Code as lead developer
metadata: 
  node_type: memory
  type: project
  originSessionId: eda14424-6e5c-4830-9811-468423d0a2ae
---

VeloCMS is a modular, multi-tenant PHP CMS being built from scratch on a dedicated server.

**Why:** Sascha wants a custom CMS with maximum AI-agent autonomy built in from day one.

**How to apply:** Always read VELOCMS_MASTERPLAN.md on the server before any coding task. That file is the single source of truth.

## Key facts
- Server: Ubuntu 26.04 LTS, IP 95.217.185.113
- SSH: `ssh -p 2222 velocms@95.217.185.113` — root login DISABLED, port 22 CLOSED
- sudo user: velocms (passwordless sudo)
- Firewall: UFW active — only ports 2222, 80, 443 open
- Fail2Ban: active, monitoring SSH
- GitHub: Sascha-Zielke/velocms (private repo)
- Codebase root on server: /var/www/velocms/
- Stack: PHP 8.5.4, MySQL 8.4, Nginx 1.28, Vanilla JS — NO frameworks
- Multi-tenancy: one site = one MySQL database (DB-level tenant isolation)
- Namespace: VeloCMS\ (PSR-4)
- MySQL velocms user password: xXP41rzY9n0haVsQILOX6F8BvREJ

## Current phase
Session 15 complete (2026-05-19). Booking Core module is FROZEN/COMPLETE.
- Production: https://webzite-newmedia.com (HTTPS, FastCGI cached)
- Admin: https://webzite-newmedia.com/admin
- CI/CD: GitHub Actions (lint → PHPUnit → SSH deploy on push to main)
- PHPUnit: 23 tests, 27 assertions, all passing

**Translation system COMPLETE (Session 16):**
- translations table in velocms_core, seeded with nav/UI strings (DE+EN)
- t() and lang() helpers global; I18n singleton in bootstrap
- Admin: /admin/translations (inline edit, auto-translate via Anthropic, bulk translate, seed)
- DE|EN toggle in admin topbar + floating frontend button — no page reload
- window.__VCMS_I18N__ injected; data-i18n on all sidebar nav links
- Anthropic API key stored in settings table (module: i18n, key: anthropic_api_key)

**Next priorities:**
1. Users module admin UI — list, create, edit, deactivate users (browser UI; CLI already exists)
2. Password reset via email (forgot-password flow)
3. API completeness — PUT/DELETE for pages and posts
4. README.md for GitHub repo
5. Booking enhancements (Stripe, Google Calendar, calendar view) — future

## Known fixes / gotchas
- Root .env (/var/www/velocms/.env) must be 0640 (velocms:www-data) so PHP-FPM can read core DB credentials. bootstrap.php loads it first, then site-specific .env.
- VeloCMS\Admin\ namespace maps to admin/controllers/ in composer.json.
- CLI dispatcher line must be `$handler->run($args); exit(0);` — not `exit($handler->run($args))` (run() returns void).

## Masterplan location
/var/www/velocms/VELOCMS_MASTERPLAN.md — covers: architecture, full feature list, DB conventions, security rules, coding standards, Git conventions, module guide, AI agent operating instructions, 6 development phases.

## Links
- [[user-sascha]] — user profile
- [[feedback-velocms]] — project-specific feedback
