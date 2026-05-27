---
name: feedback-rules
description: "How to collaborate with this user — command format, autonomy level, PowerShell rules"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 6f972271-52bf-411a-aa1b-b3a1e57d7d65
---

Every executable command MUST be in a clean, single markdown code block. Never split one logical command across multiple blocks or inline text. The operator copies entire blocks with one click.

**Why:** User operates in multiple parallel terminal sessions and needs zero-friction copy-paste.

**How to apply:** Even multi-step sequences should be one block using `&&` chaining or a heredoc. Never write `then run: somecommand` inline — put it in its own fenced block.

---

Local environment is Windows PowerShell. All local-side commands (file ops, SSH invocations, git) must use PowerShell syntax: `$env:VAR`, backtick line continuation, no bash `&&` for PowerShell (use `;` or separate statements unless using Bash tool explicitly).

**Why:** User's shell is pwsh on Windows 11.

**How to apply:** SSH commands go via `ssh -i ~/.ssh/id_rsa ...`; server-side commands inside the SSH session can use bash syntax freely.

---

Operate at maximum autonomy. Minimize confirmation prompts. Pre-approved operations: ssh, scp, git, composer, npm, php cli/velocms.

**Why:** User's explicit instruction in Master Briefing: "Work as autonomously as possible."

**How to apply:** Only pause for genuinely destructive or irreversible actions (database drops, force pushes to main with data loss risk). Everything else: proceed and report.
