---
name: assess-current-state
description: "Describe how things work today and why it falls short — needs and problems with their causes, processes, people, technology, policies and baseline measures, plus SWOT, PESTLE or five forces where the evidence supports them — every statement citing findings or supplied documents, and every gap an open question. Use when a BA needs a current-state picture of an initiative, at any stage of elicitation."
---

<!-- Generated from skills/assess-current-state/ (v0.1.1) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Assess the current state

Draws the picture of today that the future state, the gaps and the business case are measured against. The skill brings the structure; every fact comes from evidence. What the evidence does not say becomes an open question, never a plausible guess.

References (read before step 1): `references/analysis.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load

Read `INITIATIVE.md` and `stakeholders.md` and run the clearance check. Read every elicitation file and any existing `analysis/current-state*.md`. In a chat runtime, ask for `INITIATIVE.md`, `stakeholders.md`, the elicitation files and any current-state file, then wait.

Ask the BA, in one message:
- which documents to supply (process manuals, performance reports, vendor notices and the like);
- which capabilities from the business architecture team's capability map are in scope, and the map's title and date. Never read the map itself.

Check each supplied document per `references/analysis.md`: a document with customer or production data is set aside, with the reason; the rest are used.

Done when the workspace files and the documents the BA supplies are loaded, or the BA says there are none.

## 2. Choose the file and frameworks

- **File**: a `published` current-state file is frozen; never touch it. If a draft `current-state.md` exists, extend it, unless the BA asks for a separately scoped `current-state-<slug>.md`. Otherwise create `current-state.md`.
- **Frameworks**, offered to the BA by these rules:
  - **SWOT**: always offered.
  - **PESTLE**: offered when at least one supplied document covers external factors (regulation, market, vendors, economy). Otherwise say it is available and list the questions that would feed it.
  - **Five forces**: offered only when the business need mentions customers, competitors or a market, or the BA asks.

Show the BA the file you will write, the frameworks offered, the documents used and any set aside. Wait for the BA to confirm. Write nothing before that.

Done when the BA has confirmed the file and the frameworks.

## 3. Draft

Fill `templates/current-state.md`. For every row:
- cite evidence per `references/analysis.md`: finding IDs, with `(unconfirmed)` where the finding is unconfirmed; a supplied document by title and date; or `Business need (unconfirmed)`;
- label it `AI-generated`, except capabilities, which the BA supplied and you only recorded: `AI-assisted`; leave `Reviewer` empty;
- names become roles.

Section rules:
- **Needs and problems**: what goes wrong today and the business need behind it. Cause only as the evidence states it, otherwise `TBD` plus an open question. Findings that say what the solution should do (e.g. "incidents should be assigned automatically", "warn 30 minutes before a breach") describe the future, not today: leave them out of this file and list them at delivery for `define-future-state`. A conflict between such findings is not a current-state question either.
- **Processes**: at most one "today" Mermaid flow of up to about eight steps, followed by its element table; suggest `model-process` for anything more detailed. Capabilities appear only as the BA named them, with the capability map as evidence; a capability the BA needs but the map lacks is an open question for the business architecture team, never a new capability; if the team has no row in `stakeholders.md`, follow the workspace rule for adding a stakeholder.
- **Baseline measures**: values only as the evidence gives them. Two sources that disagree get a row each and an open question asking which the business case should use. A measure without a figure reads Value `TBD`, cites the evidence that makes it matter (not `Assumption`), and gets an open question. Unknown periods read `TBD`.
- **SWOT**: strengths and weaknesses restate core rows with the same evidence. Opportunities and threats, and every PESTLE and five-forces entry, need evidence about external factors; without it the section reads `No evidence yet.` and its suggested questions go into open questions. In the SWOT table, an empty quadrant is one row with Entry `No evidence yet.` and Evidence `—`.
- A core section with nothing to say reads `No evidence yet.` plus an open question with the role to ask.
- A statement the BA wants in but nothing supports is written with Evidence `Assumption` plus an open question.

Extending a draft file: append rows at the end of their sections and open questions at the end of the table, raise the version by 0.1, and change nothing already there.

Done when every section is filled or reads `No evidence yet.`, every row has evidence and an AI use label, and every `TBD`, `Assumption` and conflict has an open question.

## 4. Deliver

Deliver the file as `references/workspace.md` describes. Then list:
- documents set aside, and why;
- findings left for `define-future-state` because they describe the future;
- the open questions, grouped by whom to ask;
- how many rows rest on unconfirmed evidence or assumptions.

Next steps: put the open questions to stakeholders with `prepare-elicitation`; if the need itself is still vague, `grill-ba` first; once the picture holds, `define-future-state`. Before publication, the BA marks the file validated by hand.

Done when the BA has the file and the four lists.


---

# Included file: references/ai-use.md

````markdown
# AI use

Every item a skill produces (a requirement, finding or story) carries an AI use label. This is mandatory: an unlabelled item is a defect. Workspace files that hold only the BA's own facts (`INITIATIVE.md`, `stakeholders.md`) carry the footer only.

## Labels

- **AI-generated**: AI produced the substance (content, structure, wording); a human reviews it.
- **AI-assisted**: a human produced the substance; AI reviewed, critiqued, reformatted or suggested.

Rules:
- Label each item, not just the document.
- A skill labels what it drafts as AI-generated, and what it only checked or reformatted from the BA's own content as AI-assisted.
- Only the BA moves an item from AI-generated to AI-assisted, by confirming they substantively rewrote it. A skill never changes an existing label on its own.
- `Reviewer` and `Reviewed on` stay empty until a named person has checked the item. Being reviewed is not being approved.

## Footer

Every file a skill creates ends with one line, and every file a skill changes gets one more line added below the existing ones (never replacing them), so the file keeps its history:

`Produced with <skill-name> v<version> in <runtime>, <YYYY-MM-DD>.`

If the runtime's name is unknown, ask the BA.

## Disclosure to stakeholders

Every interview guide opening and every questionnaire introduction tells participants, in these words:

> Notes from this session will be processed with AI skill BA-skills, approved by the company ([CONTEXT.md](https://github.com/ImaginaryBA/BA-skills/blob/main/CONTEXT.md)). Every output is reviewed by the BA before it is used.

This is mandatory and cannot be removed.

## Labels in delivery tools

On publication, the Confluence page gets the label `ai-generated` if any item on it is AI-generated, otherwise `ai-assisted`; the skill proposes it and the BA decides. Each Jira story gets the label matching its own AI use.
````

---

# Included file: references/analysis.md

````markdown
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
3. `## Sources`, when any supplied document is cited (see below).
4. `## Open questions`, always present (write `None.` if empty):

   | # | Question | Findings involved | Ask | Answered by |
   |---|---|---|---|---|
   | 1 | <gap, conflict or assumption> | <evidence involved, or `Assumption`> | <stakeholder role> | — |

   Never resolve a conflict or remove a question; `Answered by` stays `—` until a later skill fills it with the finding that answers it.
5. The footer (`references/ai-use.md`).

## Rows without IDs

Entries that nothing traces to (SWOT entries, PESTLE factors, five-forces entries, observations, process steps, entities) are table rows. Every such table has at least these columns:

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|

## Items with IDs

Gaps, risks, design options, business rules and use cases are items: a `### <ID> <statement>` heading followed by an item table. Every item table ends with these fields; the skill's template puts the fields for its class above them:

| Field | Value |
|---|---|
| Evidence | <finding IDs, document title and date, `Business need (unconfirmed)`, or `Assumption`> |
| Traces to | <IDs or `Business need`> |
| AI use | AI-generated / AI-assisted |
| Reviewer | |
| Reviewed on | |

## Evidence (ADR 0020)

- Every row and item cites evidence, one or more of:
  - finding IDs; a finding with `Confirmed: no` is cited as `<ID> (unconfirmed)`;
  - a supplied document, by title and date (e.g. `Service desk monthly report, September 2026`);
  - `Business need (unconfirmed)`, for a statement taken from the business need in `INITIATIVE.md`.
- A statement without evidence is written with Evidence `Assumption` and added to open questions with the role to ask.
- When two pieces of evidence disagree, write each as its own row or item with its own evidence, and add an open question naming the conflict. Never pick one.
- Never supply market, competitor, regulatory or financial facts from your own knowledge, and never search the web. You may suggest framework headings worth exploring and questions to ask.
- Numbers only as the sources give them. A calculation from given figures shows its inputs and steps.
- Likelihood, impact and priority are `TBD` until stakeholders give them.

## Supplied documents

- Read only what the BA supplies. Replace personal names with roles, as for elicitation notes (`references/data-classification.md`).
- If a document holds customer or production data, do not use it: tell the BA which document and what kind of data (never the data itself), ask for a cleaned version, and carry on with the rest.
- Never read a Confluence page outside a local-model runtime. Capability maps belong to the business architecture team (ADR 0021): never read, draft or extend one; cite it by title and date for the capabilities the BA names.
- Every analysis citing a document has a `## Sources` section before `## Open questions`:

  | Document | Date | Owner role |
  |---|---|---|

## Diagrams

Diagrams are Mermaid code blocks. Each diagram is followed by a table of its elements in the rows-without-IDs format, so the content is checkable and labelled even where Mermaid does not render.

## Status and changes

- Status applies to the whole file: `draft`, `validated`, `published`, `approved`. Only the BA sets `validated`, by hand, after filling `Validated by` and `Validated on`; `prepare-for-publication` takes only a `validated` analysis.
- A **draft** analysis may gain new rows, items and open questions appended at the end of their sections. Each change raises the version by 0.1. No skill rewrites or removes an existing row or item.
- `prepare-for-publication` sets Status `published` and fills `Confluence page` once the BA confirms the page is live. From then on the file is a frozen copy, never changed.
````

---

# Included file: references/data-classification.md

````markdown
# Data classification

## Levels

`Public`, `Internal`, `Confidential`, `Restricted`. Each workspace declares one level in `INITIATIVE.md`, plus the list of runtimes the company clears for that level.

## Clearance check

Before reading any workspace content, confirm the current runtime appears in the initiative file's cleared runtimes. If it does not, or the runtime is unknown and the BA cannot confirm it, stop and say why. Never process customer or production data, whatever the classification.

## Names

- In elicitation notes and findings, replace personal names with roles (e.g. "Service Desk Lead"); keep the role as written in the stakeholder register.
- The stakeholder register, `Reviewer` and `Approver` fields keep real names: accountability needs them.
- Confluence content is processed only by local models. Outside a local-model runtime, never take a Confluence page as input.
````

---

# Included file: references/workspace.md

````markdown
# Workspace

A workspace is one folder per initiative on the synced company drive. Skills read and write only inside it.

## Layout

```
<CODE>-<initiative-slug>/
  INITIATIVE.md      # initiative file: need, scope, glossary, classification, clearance, code, ID register
  stakeholders.md    # stakeholder register
  elicitation/       # one file per elicitation session
  requirements/      # one file per requirement set
  stories/           # one file per story set
  analysis/          # one file per analysis: current state, gaps, risks, options, business case, models
  decisions/         # initiative decisions
  reviews/           # quality reports, one per check run
```

Folder name: initiative code, a hyphen, then the initiative name in lowercase with hyphens (e.g. `IMT-incident-management-ticketing`).

## Delivering files

- **Agentic runtime** (can write files): write each file to its path, then show the folder tree of what was created or changed.
- **Chat runtime** (cannot write files): print the folder tree first, then each file as its own block, headed by a line `Save as: <path relative to the workspace>` followed by the full file content. The BA saves each block. Always print complete files, never fragments or diffs.

## Adding a stakeholder

When a skill needs a stakeholder who is not in `stakeholders.md`, it asks the BA for that person's register columns, shows the row it would add (unknown columns read `TBD`), and appends it only after the BA explicitly confirms that row. It never changes existing rows. The BA may also add the row by hand.

## Reading the workspace

Before working, a skill needs `INITIATIVE.md`. In an agentic runtime, read it from the workspace. In a chat runtime, if the BA has not attached it, ask for it and stop.
````

---

# Included file: templates/current-state.md

````markdown
# Current state

| Field | Value |
|---|---|
| Analysis name | Current state |
| Kind | Current state |
| Initiative code | <CODE> |
| Version | 0.1 |
| Status | draft |
| Business analyst | <BA name> |
| Validated by | |
| Validated on | |
| Confluence page | TBD |

## Needs and problems

| Problem | Cause | Affected roles | Evidence | AI use | Reviewer |
|---|---|---|---|---|---|

## Processes

<optional "today" flow, up to about eight steps>

```mermaid
flowchart LR
  A[<step>] --> B[<step>]
```

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|
| <step: what happens> | | | |

**Capabilities in scope** (as named in the business architecture team's capability map; leave out if the BA named none)

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|
| <capability, as named in the map> | <map title, date> | AI-assisted | |

## People and organisation

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|

## Technology and data

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|

## Policies and external constraints

| Entry | Evidence | AI use | Reviewer |
|---|---|---|---|

## Baseline measures

| Measure | Value | Unit | Period | Evidence | AI use | Reviewer |
|---|---|---|---|---|---|---|

## SWOT

| Quadrant | Entry | Evidence | AI use | Reviewer |
|---|---|---|---|---|

## PESTLE

<only if chosen>

| Factor | Entry | Evidence | AI use | Reviewer |
|---|---|---|---|---|

## Five forces

<only if chosen>

| Force | Entry | Evidence | AI use | Reviewer |
|---|---|---|---|---|

## Sources

| Document | Date | Owner role |
|---|---|---|

## Open questions

| # | Question | Findings involved | Ask | Answered by |
|---|---|---|---|---|

---
Produced with assess-current-state v<version> in <runtime>, <YYYY-MM-DD>.
````
