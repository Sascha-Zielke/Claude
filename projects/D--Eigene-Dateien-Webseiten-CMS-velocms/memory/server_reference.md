---
name: server-reference
description: "VeloCMS server IPs, paths, DB names, SSH access for Hetzner VPS"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 6f972271-52bf-411a-aa1b-b3a1e57d7d65
---

**Hetzner VPS:**
- IP: 95.217.185.113
- SSH user (production): velocms
- SSH user (initial root provisioning): root
- SSH key (local): ~/.ssh/id_rsa
- Port: 22

**Domain:** webzite-newmedia.com  
**Admin URL:** https://webzite-newmedia.com/admin

**Server Paths:**
- Webroot: /var/www/velocms/public
- App root: /var/www/velocms
- Tenant storage: /storage/tenants/{tenant_id}/uploads/
- Logs: /var/log/velocms/

**Databases:**
- Master registry: velocms_master (vcms_sites table)
- First tenant site: velocms_site_1
- App DB user: velocms_app

**GitHub:**
- Repo: https://github.com/Sascha-Zielke/velocms
- Skills repo: https://github.com/Sascha-Zielke/velocms-skills
- Deploy via: GitHub Actions → SSH to VPS → git pull + restart PHP-FPM
