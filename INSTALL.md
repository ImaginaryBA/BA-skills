# Installing BA-skills

Each skill is a folder under `skills/` holding a `SKILL.md` plus `references/` and `templates/`. Install the **whole folder** of every skill you want; the skill reads the files beside it.

Get the library first:

```
git clone https://github.com/ImaginaryBA/BA-skills
```

Skill locations differ by tool and change between versions. The paths below were current when written; if a skill does not appear, check your tool's documentation for its skills folder.

## Agentic runtimes

Copy (or symlink) every folder in `BA-skills/skills/` into the tool's skills folder, then restart the tool. Use the user-level folder to have the skills in every initiative, or the project folder to scope them to one workspace.

| Tool | User-level folder | Project folder |
|---|---|---|
| Claude Code | `~/.claude/skills/` | `<workspace>/.claude/skills/` |
| Codex | `~/.codex/skills/` | — |
| Antigravity | `~/.gemini/config/skills/` | `<workspace>/.agents/skills/` |
| Pi | `~/.pi/agent/skills/` or `~/.agents/skills/` | `<workspace>/.pi/skills/` or `<workspace>/.agents/skills/` |

Example (Claude Code, macOS or Linux):

```
mkdir -p ~/.claude/skills
cp -R BA-skills/skills/* ~/.claude/skills/
```

Check: open your initiative's folder in the tool and ask "Use ask-ba: where am I?".

## Chat runtimes (Open WebUI)

Open WebUI imports a skill as one markdown file, so each skill is also published as a single file with its references and templates included: `dist/open-webui/<skill>.md`.

1. In Open WebUI, open **Workspace → Skills** and choose **Import**.
2. Select a file from `BA-skills/dist/open-webui/`; its name and description fill in from the file. Repeat for each skill you want.
3. In a chat, type `$` and pick the skill to load it, then attach the workspace files the skill asks for (`ask-ba` lists them).

Open WebUI cannot write files: each skill prints every file it creates or changes as a block headed `Save as: <path>`. Save each block into your workspace folder.

Only use Open WebUI for an initiative whose `INITIATIVE.md` lists it as a cleared runtime.

## Updating

Pull the latest library and copy the skill folders again. Each skill's version is in its `SKILL.md` header, and every file a skill writes records the skill and version that produced it.
