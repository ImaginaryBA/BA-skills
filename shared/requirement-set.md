# Requirement set

A requirement set is one file in `requirements/`, published later as one Confluence page. File name: the set name as a lowercase hyphenated slug (e.g. `incident-logging-and-categorisation.md`).

Business requirements always live in their own set, `requirements/business-requirements.md`. Feature sets hold SR, FR, NFR and TR items and trace to it.

## File layout

1. `# <Set name>`, then the set header table:

   | Field | Value |
   |---|---|
   | Set name | <name> |
   | Initiative code | <CODE> |
   | Version | 0.1 |
   | Status | draft |
   | Business analyst | <BA name> |
   | Confluence page | TBD |

2. One `## <Class name>` section per class present, in the order BR, SR, FR, NFR, TR.
3. Items, each a `### <ID> <statement>` heading followed by its item table.
4. `## Open questions`, always present (write `None.` if empty).
5. The footer (`references/ai-use.md`).

## Item table

| Field | Value |
|---|---|
| Class | BR / SR / FR / NFR / TR |
| Status | draft |
| Priority | TBD |
| Rationale | <one sentence: why it exists> |
| Threshold | <measurable condition, or TBD> |
| Source | <finding IDs; for a BR, may also be `Business need`> |
| Traces to | <IDs this item satisfies> |
| Reused from | — |
| AI use | AI-generated / AI-assisted |
| Reviewer | |
| Reviewed on | |

## Statements

| Class | Pattern | Example |
|---|---|---|
| BR | A measurable outcome | Reduce incidents breaching resolution service levels to below 5% within 6 months of go-live. |
| SR | `<Stakeholder role> needs to …` | Service Desk Lead needs to see every incident at risk of breaching its service level. |
| FR | `The system shall …` | The system shall create an incident from each critical monitoring alert. |
| NFR | `The system shall …` | The system shall return incident search results within 2 seconds. |
| TR | `Before go-live, …` / `During cutover, …` | Before go-live, all open legacy tickets shall be migrated with their full history. |

One requirement per statement. Use the initiative glossary's terms.

## Field rules

- **Rationale**: mandatory, one sentence, drawn from the source findings. When the sources do not say why, write `TBD` and add an open question.
- **Threshold**: the measurable condition that proves the item is met (e.g. "95% of searches return in ≤ 2 s"). Mandatory for BR and NFR: only numbers the sources give, otherwise `TBD` plus an open question. Optional for SR, FR and TR: `—` when none applies.
- **Priority**: always `TBD` at creation; prioritisation is a stakeholder decision.
- **Source**: finding IDs. A BR drafted from the initiative's business need may cite `Business need`.
- **Traces to**: SR, FR, NFR and TR trace to at least one BR; an FR may also trace to the SR it satisfies. A BR traces to `Business need`.
- **Status** values, in order: `draft`, `verified`, `validated`, `published`, `approved`, then `retired` or `superseded`.

## Open questions

A table at the end of the set:

| # | Question | Findings involved | Ask |
|---|---|---|---|
| 1 | <conflict, gap or missing rationale or threshold> | <finding IDs> | <stakeholder role> |

Conflicts between findings are listed here and never resolved by a skill.

## Changing a set

- A **draft** set may gain new items and open questions appended at the end of their sections. Existing items are never edited or removed by a skill. Each change raises the version by 0.1.
- A **published** set is a frozen copy: never changed. New needs go into a new set.
