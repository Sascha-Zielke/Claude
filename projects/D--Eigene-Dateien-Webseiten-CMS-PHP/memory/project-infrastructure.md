---
name: project-infrastructure
description: "VeloCMS server, SSH, database, GitHub, domain — alle Infra-Details für autonome Arbeit"
metadata: 
  node_type: memory
  type: project
  originSessionId: 793cb0fe-6003-45e0-8f3d-133234777e17
---

# VeloCMS Infrastructure

## Server
- **Hetzner VPS**, Ubuntu, IP: `95.217.185.113`
- **SSH User:** `velocms` · **Port:** `2222`
- **SSH Key (lokal):** `C:\ssh\id_ed25519` (existiert auf dem Entwickler-Rechner)
- **SSH Passwort (fallback):** in `D:\Eigene Dateien\Webseiten\CMS\PHP\SSH.txt`
- **Webroot:** `/var/www/velocms`
- **PHP:** 8.2+ · **Webserver:** Nginx · **DB:** MySQL 8

## SSH-Verbindung
```powershell
ssh velocms@95.217.185.113
```
⚠️ **Port ist 22** (nicht 2222 — alter Eintrag war falsch)

## Datenbank
- **Master-DB:** `velocms_master`
- **App-User:** `velocms_app`
- **App-Passwort:** `VeloCMS_DB_Secure_2026!`
- **Root-Passwort:** in SSH.txt (nur Notfall)
- **MySQL-Verbindung:**
```bash
mysql -u velocms_app -p'VeloCMS_DB_Secure_2026!' velocms_master
```

## GitHub
- **Repo:** https://github.com/Sascha-Zielke/velocms
- **Token:** in `D:\Eigene Dateien\Webseiten\CMS\PHP\GitHub-Token.txt`
- **Server Deploy-Key Public:** `ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDIUnK2SICD9zGKKJ2nk0PcoU+NWpVBdR+A6+gXG/piH`
- **Key-Pfad auf Server:** `/home/velocms/.ssh/github_deploy`
- **Deploy-Ziel:** push → main → GitHub Actions → `/var/www/velocms`

## Domain & Admin
- **Domain:** https://webzite-newmedia.com
- **Admin-URL:** https://webzite-newmedia.com/admin
- **CMS-Login Email:** s.zielke84@gmail.com
- **CMS-Passwort:** in `D:\Eigene Dateien\Webseiten\CMS\PHP\CMS.txt`

## Lokales Arbeitsverzeichnis
- `D:\Eigene Dateien\Webseiten\CMS\PHP\`
- Plandateien: `resume.md`, `task_plan.md`
- Skills: `Skills\velocms-skills\skills\`

## Server-State (Stand: 2026-05-26)
**PRODUCTION — Phasen 0–16 live.** Vollständig deployed, CI/CD läuft grün.

- PHP 8.2.31 · Nginx 1.18 · MySQL 8.0.45 · Composer 2.9.8
- CI: GitHub Actions Run #9 — ✅ 30 Tests, auto-deploy auf push→main
- Laufende Module: Auth, Pages (Visual Editor), Blog, Media, Navigation, Settings, Users, SEO, Error-Pages
- Superadmin: s.zielke84@gmail.com
- DB: `velocms_master` (Tenant-Registry) + `velocms_site_a` (Site-DB)

## CI/CD — Bekannte Stolperfallen
- **PAT hat keinen `workflow` scope** → `.github/workflows/ci.yml` NICHT per git push änderbar; nur über GitHub Web-UI
- **PHPUnit 11: kein `--no-interaction` Flag** — dieser Flag existiert nicht, führt zu Exit-Code 2
- **PHPUnit 11: `colors` ist xs:boolean** → nur `"true"` oder `"false"`, NICHT `"auto"` / `"always"` / `"never"`
- **Nach root-SSH-Git-Befehlen:** `.git/` bekommt root-Ownership → deploy-User `velocms` kann nicht mehr pushen/pullen
  - Fix: `chown -R velocms:velocms /var/www/velocms/.git`
- **Server-Remote muss SSH bleiben:** `git@github.com:Sascha-Zielke/velocms.git` (nicht HTTPS)
