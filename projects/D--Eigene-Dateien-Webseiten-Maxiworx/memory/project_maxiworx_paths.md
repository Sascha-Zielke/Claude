---
name: project-maxiworx-paths
description: Correct paths for the Maxiworx project — working dir and XAMPP dev folder
metadata: 
  node_type: memory
  type: project
  originSessionId: 735dc771-df3d-4da6-8263-ba7816a0737a
---

The canonical working directory for the Maxiworx project is:
`D:\Eigene Dateien\Webseiten\Maxiworx\`

**Why:** The user clarified this explicitly after files were initially confirmed at the correct path. XAMPP local dev folder at `D:\Eigene Dateien\Wilde_Jungs\xampp\htdocs\maxiworx\` is the legacy/local dev location — project files have been consolidated into the Webseiten path.

**How to apply:** Always use `D:\Eigene Dateien\Webseiten\Maxiworx\` for all file operations, commands, and path references. Never write to or assume the XAMPP htdocs path.
