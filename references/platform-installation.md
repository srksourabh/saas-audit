# Platform Installation Reference

Copy the complete repository because `SKILL.md` depends on relative files in `references`, `assets`, `scripts` and `docs`.

## Standard destinations

| Client | User-level path | Project-level path |
|---|---|---|
| Codex / Agent Skills / Anti-Gravity | `~/.agents/skills/saas-audit/` | `<project>/.agents/skills/saas-audit/` |
| Claude Code | `~/.claude/skills/saas-audit/` | `<project>/.claude/skills/saas-audit/` |
| VS Code / GitHub Copilot | Client-dependent | `<project>/.github/skills/saas-audit/` |
| Hermes | Configured skills directory | Configured project skills directory |

## Automatic installers

macOS, Linux, WSL or Git Bash:

```bash
git clone https://github.com/srksourabh/saas-audit.git
cd saas-audit
./install.sh
```

Windows PowerShell:

```powershell
git clone https://github.com/srksourabh/saas-audit.git
Set-Location saas-audit
.\install.ps1
```

Use `--project` or `-Project` for project-local installation.

## Hermes

Set `HERMES_SKILLS_DIR` before running the installer or pass `-HermesSkillsDir` to PowerShell. When no conventional skill directory exists, direct the agent to read `SKILL.md` in the cloned repository.

## Verification

Confirm `SKILL.md` and all linked references exist. Ask the client to describe the skill's operating modes and safety boundaries before granting terminal, browser or infrastructure permissions.

The skill uses only permissions already granted to the AI client. Installation does not authorize testing and does not create production access.
