<!-- Generated from shared/analysis.md by scripts/sync_shared.py. Edit the master, not this copy. -->

# Analysis

An analysis is one file in `analysis/` (ADR 0017), published later as one Confluence page (ADR 0019). File name: `<kind>.md`, or `<kind>-<slug>.md` when the initiative has more than one of that kind.

| Kind | File | ID'd items |
|---|---|---|
| Current state (with SWOT, PESTLE, five forces as needed) | `current-state.md` | — |
| Future state and gaps | `future-state.md` | GP |
| Risks | `risks.md` | RK |
| Design options | `design-options.md` | OP |
| Business case | `business-case.md` | — (cites OP, RK, GP) |
| Process model | `process-<slug>.md` | — |
| Use cases and scenarios | `use-cases-<slug>.md` | UC |
| Data model | `data-model.md` | — |
| Business rules | `business-rules.md` | RL |

## File layout

1. `# <Analysis name>`, then the header table:

   | Field | Value |
   |---|---|
   | Analysis name | <name> |
   | Kind | <kind from the table above> |
   | Initiative code | <CODE> |
   | Version | 0.1 |
   | Status | draft |
   | Business analyst | <BA name> |
   | Validated by | <stakeholder roles, filled by the BA> |
   | Validated on | <YYYY-MM-DD, filled by the BA> |
   | Confluence page | TBD |

2. The sections the skill's template defines for its kind.
3. `## Open questions`, always present (write `None.` if empty), in the requirement set's format, with `Findings involved` holding finding IDs or `Assumption`.
4. The footer (`references/ai-use.md`).

## Rows without IDs

Entries that nothing traces to (SWOT entries, PESTLE factors, five-forces entries, observations, process steps, entities) are table rows. Every such table has at least these columns:

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|

## Items with IDs

Gaps, risks, design options, business rules and use cases are items: a `### <ID> <statement>` heading followed by an item table. Every item table ends with these fields; the skill's template puts the fields for its class above them:

| Field | Value |
|---|---|
| Evidence | <finding IDs, or document title and date, or `Assumption`> |
| Traces to | <IDs or `Business need`> |
| AI use | AI-generated / AI-assisted |
| Reviewer | |
| Reviewed on | |

## Evidence (ADR 0020)

- Every row and item cites evidence: finding IDs, or a document the BA supplied, named by title and date.
- A statement without evidence is written with Evidence `Assumption` and added to open questions with the role to ask.
- Never supply market, competitor, regulatory or financial facts from your own knowledge, and never search the web. You may suggest framework headings worth exploring and questions to ask.
- Numbers only as the sources give them. A calculation from given figures shows its inputs and steps.
- Likelihood, impact and priority are `TBD` until stakeholders give them.

## Diagrams

Diagrams are Mermaid code blocks. Each diagram is followed by a table of its elements in the rows-without-IDs format, so the content is checkable and labelled even where Mermaid does not render.

## Status and changes

- Status applies to the whole file: `draft`, `validated`, `published`, `approved`. Only the BA sets `validated`, by hand, after filling `Validated by` and `Validated on`.
- A **draft** analysis may gain new rows, items and open questions appended at the end of their sections. Each change raises the version by 0.1. No skill rewrites or removes an existing row or item.
- `prepare-for-publication` sets Status `published` and fills `Confluence page` once the BA confirms the page is live. From then on the file is a frozen copy, never changed.
