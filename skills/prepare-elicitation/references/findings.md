<!-- Generated from shared/findings.md by scripts/sync_shared.py. Edit the master, not this copy. -->

# Findings

A finding is one statement from elicitation, attributed to a stakeholder role. Every requirement's `Source` is one or more finding IDs.

## Elicitation file

One file per session or source document in `elicitation/`, named `<YYYY-MM-DD>-<slug>.md` (e.g. `2026-10-12-service-desk-workshop.md`). It starts with a header table (Source, Date, Participants as roles) and grows through the session's life, each section added by the skill that owns it:

1. `## Plan` and `## Interview guide` or `## Questionnaire`: `prepare-elicitation`.
2. `## Notes`: the BA's notes or transcript, then `notes-to-findings`.
3. `## Findings`: the findings table below.

A file made from raw input or a workshop may hold only the header and `## Findings`.

| ID | Finding | Stakeholder role | Confirmed (yes/no) | AI use |
|---|---|---|---|---|
| IMT-FN-004 | Agents re-key critical monitoring alerts into the ticketing tool by hand. | Service Desk Lead | yes | AI-generated |

- **ID**: from the ID register, class `FN` (`references/ids.md`).
- **Finding**: one statement, in the stakeholder's meaning, without names (`references/data-classification.md`).
- **Stakeholder role**: as written in `stakeholders.md`.
- **Confirmed**: `yes` only when the stakeholder has confirmed the BA's understanding of it.
- **AI use**: per `references/ai-use.md`.

Only confirmed findings become requirements. Unconfirmed findings become open questions.
