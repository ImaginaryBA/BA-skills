# BA-skills

Agent skills for business analysis, aligned with BABOK® v3: elicitation, requirements, verification, publication and delivery stories, each step traceable and every AI contribution labelled.

Skills run in Claude Code, Codex, Antigravity, Pi and similar agentic tools, and in chat tools such as Open WebUI. A human business analyst stays accountable for every output.

## Start here

Install the skills ([INSTALL.md](INSTALL.md); Open WebUI users import the single-file versions in [`dist/open-webui/`](dist/open-webui/)), open your initiative's folder, and ask **`ask-ba`**: "Where am I and what next?"

## The skills

| Skill | Use it when you… |
|---|---|
| `ask-ba` | are unsure which skill fits, or want a status of your initiative |
| `set-up-initiative` | start a new piece of analysis work |
| `grill-ba` | have a vague need to sharpen before elicitation |
| `prepare-elicitation` | are about to interview or survey stakeholders |
| `notes-to-findings` | have session notes or a transcript, or stakeholders replied to a confirmation |
| `findings-to-requirements` | want requirements from confirmed findings or raw material |
| `check-requirement-quality` | want draft requirements reviewed and verified |
| `prepare-for-publication` | have a validated set to send for approval in Confluence |
| `requirements-to-stories` | need Jira stories from validated requirements |

BABOK coverage per task: [`skills/ask-ba/references/coverage.md`](skills/ask-ba/references/coverage.md).

## How it works

- Each initiative lives in a **workspace**: a folder of markdown files (`INITIATIVE.md`, `stakeholders.md`, `elicitation/`, `requirements/`, `stories/`, `reviews/`, `decisions/`, `analysis/`). See [`workspace-example/`](workspace-example/) for a complete fictional initiative.
- Every item a skill drafts is labelled **AI-generated** or **AI-assisted**, and every interview or questionnaire tells stakeholders that AI is used.
- Requirements become the system of record in Confluence once published; after that, no skill touches them.

## For contributors

- Vocabulary: [`CONTEXT.md`](CONTEXT.md). Decisions: [`docs/adr/`](docs/adr/). Roadmap: [`PLAN.md`](PLAN.md).
- Rules shared by several skills live once in [`shared/`](shared/); run `python3 scripts/sync_shared.py` after editing them or any skill (and `--check` before committing). It also regenerates the BABOK coverage table and `dist/open-webui/`.
- Each skill has test cases in [`evals/`](evals/).

BABOK® is a registered trademark of the International Institute of Business Analysis (IIBA). This project is not affiliated with IIBA and cites BABOK by section number and name only.
This project is released under the [MIT License](LICENSE).
