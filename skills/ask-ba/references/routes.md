# Routes

Authored here, not generated from `shared/`. Match the BA's situation to one row; when two rows fit, name both in the order given.

| The BA's situation | Skill | Files to attach in a chat runtime |
|---|---|---|
| Starting new work; no `INITIATIVE.md` exists | `set-up-initiative` | none |
| The need is vague, or open questions keep piling up | `grill-ba` | `INITIATIVE.md`, `stakeholders.md`, elicitation files |
| Needs a picture of how things work today and why it falls short (current state, SWOT, PESTLE, baselines) | `assess-current-state` | `INITIATIVE.md`, `stakeholders.md`, elicitation files, supplied documents, any current-state file |
| About to interview or survey stakeholders | `prepare-elicitation` | `INITIATIVE.md`, `stakeholders.md`, draft requirement sets, elicitation files |
| Has notes or a transcript from a session; or stakeholders replied to a confirmation request | `notes-to-findings` | `INITIATIVE.md`, `stakeholders.md`, the session's elicitation file, draft requirement sets |
| Has confirmed findings, or raw notes, emails or documents, and wants requirements | `findings-to-requirements` | `INITIATIVE.md`, `stakeholders.md`, elicitation files, draft requirement sets |
| Has draft requirements to review or verify | `check-requirement-quality` | `INITIATIVE.md`, the draft sets, `business-requirements.md`, the elicitation files they cite |
| Has a validated set or analysis (e.g. a business case) to send for approval; or the page is live and the file must be frozen | `prepare-for-publication` | `INITIATIVE.md`, the set or analysis |
| Has validated or published requirements and needs Jira stories; or has Jira keys to record | `requirements-to-stories` | `INITIATIVE.md`, `stakeholders.md`, the set, `business-requirements.md`, the story set |
| Wants to know what BA-skills covers | this skill, `references/coverage.md` | none |

## No skill, by design

- **Marking a set validated**: the BA does it by hand after stakeholders confirm it (fill `Validated by`, `Validated on`, set each item's Status).
- **Changing a published set**: only in Confluence, by hand; no skill touches it.
- **Adding a stakeholder or glossary term outside a skill run**: by hand, or ask the skill that needs it.
