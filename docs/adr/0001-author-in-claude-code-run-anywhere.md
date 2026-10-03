# Author in Claude Code; BAs run skills in any of several runtimes

Skills are written and evaluated in Claude Code. Other BAs may run them in Codex, Antigravity, Open WebUI, or another LLM tool. So skills must be portable: no skill may rely on git, a shell, Claude-only features (hooks, subagents, Claude-specific tool names), or a harness enforcing behaviour. Every rule a skill must follow, including the AI provenance label, is written in the skill's own instructions and output templates.
