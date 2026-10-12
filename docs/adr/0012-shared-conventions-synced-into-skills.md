# Shared conventions live in one master and are copied into each skill

Rules every skill follows (provenance, requirement-set format, ID scheme, lifecycle, data classification) are written once under `shared/`. Before a release, a script run by the library author copies the sections each skill needs into that skill's `references/` folder. Each installed skill is then self-contained in every runtime, while each rule still has a single source of truth. We rejected copying by hand into every skill (copies drift) and a separate conventions skill (chat-runtime users would have to attach two files every time).

Layout: `skills/<skill-name>/` (with `SKILL.md`, `references/`, `templates/`), `shared/`, `evals/<skill-name>/`, `workspace-example/`. Skill frontmatter holds `name`, a situation-first `description`, and `metadata` with `version`, `babok` (BABOK v3 section numbers and names only, never quoted text), `inputs` and `outputs`.
