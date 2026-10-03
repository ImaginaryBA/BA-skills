# One portable SKILL.md source, with full and manual support levels

Each skill is written once as a portable `SKILL.md` in the open Agent Skills format. In an agentic runtime it triggers by itself and reads and writes the workspace; in a chat runtime the BA attaches the skill and its inputs and saves the output. So every skill declares its inputs and outputs explicitly and never depends on reaching the workspace itself. Generated per-runtime adapters (e.g. Open WebUI prompts or model presets) are deferred to a future version, to be built only for a runtime real users depend on.
