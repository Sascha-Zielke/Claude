---
name: Maxiworx Project Overview
description: Core facts about the Maxiworx recording studio web platform — stack, paths, architecture, and what's built
type: project
originSessionId: 9093b0bc-b05f-47a1-a1aa-12fefc013db3
---
Full-stack web platform for Matthias Kupka / Studio Wahlstedt (professional sound engineer). Built May 2026.

**Why:** Professional recording studio showcase with CMS for Matthias to manage content himself.

**How to apply:** When working on this project, all paths and patterns below are authoritative.

## Paths
- XAMPP root: `D:/Eigene Dateien/Wilde_Jungs/xampp/htdocs/maxiworx/`
- URL base: `/maxiworx/`

## Stack
- PHP 8.2+ (OOP, PDO, Modular Monolith) — no frameworks
- MySQL 8.x (InnoDB, JSON columns) — CMS backend
- Vanilla JS (ES2024) — no frontend frameworks
- CSS custom properties design system (no Tailwind in production, was considered)
- GSAP ScrollTrigger for hero animation
- Google Fonts: Cormorant Garamond (display) + Inter (body)

## Files built (all complete)
- `index.php` — homepage (hero, slideshow, about, contact)
- `studio.php` — room descriptions (Live Room, Control Room, Isolation Booth, Artist Lounge)
- `equipment.php` — gear catalog (SSL 4000E, mics, outboard, monitoring, instruments)
- `sessions.php` — pricing, packages, FAQ accordion
- `specials.php` — 4 split-card specials (personal song, vocal coaching, mobile recording, event)
- `references.php` — artist grid (8 featured + 38 expandable), companies, Spotify banner
- `booking.php` — 4-step booking wizard with fetch to backend
- `css/design-system.css` — full design token system + layout
- `css/components.css` — hamburger, mobile nav, page hero, room cards, booking CTA
- `js/nav.js` — nav scroll effect, hero animation, hamburger, slideshow, scroll reveal
- `js/i18n.js` — DE/EN translation switcher (skips elements with data-cms-key)
- `includes/nav.php` — reusable nav + hamburger + mobile overlay
- `includes/page-template.php` — HTML head + nav include (used by all subpages)
- `includes/page-footer.php` — footer + social links + script tags
- `php/contact.php` — contact form handler (JSON response)
- `php/booking-submit.php` — booking wizard POST handler (JSON response)
- `cms/includes/cms-content.php` — CMS helper functions (cmsContent, c, cRaw, cmsPriceBlock, cmsFlag, cmsMedia)

## Design System
- Background: #080808 base, fixed parallax layer `.bg-fixed` (z-index: 0)
- Gold: #C8922A primary, #D4A843 hover
- Blue CTA only: #3A7BD5
- Nav: glassmorphism pill, fixed top:16px, becomes `.nav--scrolled` at 40px scroll
- Hero: MAXIWORX title, letter-spacing 0.20em, clamp(4.5rem, 13vw, 10rem)
- All sections use `position: relative; z-index: 10` to float above fixed BG

## Key architecture notes
- `index.php` is standalone (has its own inline nav/footer styles, does NOT use page-template.php)
- All subpages use `require 'includes/page-template.php'` pattern
- CMS require must come BEFORE page-template require in pages that use it (sessions.php fixed)
- `nav.js` adds class `nav--scrolled` (not BEM `site-nav--scrolled`) — design-system.css updated to match
- i18n.js skips elements with `data-cms-key` attribute to avoid overwriting CMS content
- Slideshow captions use `data-caption-de` and `data-caption-en` data attributes

## CMS (Phase 2 planned)
- Feature flags: `show_prices`, `show_faq` stored in `cms_settings` table
- Content editable via `cms/` admin panel
- `cmsPriceBlock($c, 'recording', $lang)` renders price or "auf Anfrage" based on DB flag
