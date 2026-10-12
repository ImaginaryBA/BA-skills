---
name: prepare-for-publication
description: "Turn a validated requirement set into a page ready to paste into Confluence Data Center — page properties, trimmed item blocks, open questions and a proposed AI use label — then, once the BA confirms the page is live, freeze the workspace file as published. Use when a BA is ready to send a requirement set for approval in Confluence."
---

<!-- Generated from skills/prepare-for-publication/ (v0.1.1) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Prepare for publication

Produces the page that goes to Confluence for approval, then freezes the workspace file. After this skill, the set lives in Confluence and no skill touches it again.

References (read before step 1): `references/page-format.md`, `references/requirement-set.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Check the set is ready

Read `INITIATIVE.md`, run the clearance check, and read the one set the BA names. In a chat runtime, ask for both files and wait.

The set is ready when all of these hold:
- its status is `draft` (a `published` set is already frozen: stop);
- every item's status is `validated`;
- `Validated by` and `Validated on` in the set header are filled.

If any fails, list every blocker by item ID and stop. If an item traces to a BR that is not yet validated, say so as a warning; it does not block.

Done when the set passes all three conditions.

## 2. Build the page

Fill `templates/confluence-page.md` following `references/page-format.md`: title, Part 1, Part 2, open questions if any, footer. Propose the page label. Copy statements, rationale, thresholds and sources exactly as they are in the set; this skill rewords nothing.

Done when every item in the set appears on the page, in class order, with its trimmed table.

## 3. Hand over

Show the BA the page, the proposed label and the paste steps from `references/page-format.md`. The page is shown in the chat, not saved: the frozen set is the workspace record.

Ask the BA to confirm the label, publish the page, and reply with its link. Wait. Change nothing in the workspace before the BA replies.

Done when the BA has replied with the page link.

## 4. Freeze the set

Only after the BA confirms the page is live:
- set the set header's Status and every item's Status to `published`;
- fill `Confluence page` with the link;
- add this skill's footer line (`references/ai-use.md`);
- leave everything else exactly as it was, version included.

Deliver the frozen set as `references/workspace.md` describes. Tell the BA that approval now happens in Confluence, that this file is a frozen copy no skill will change, and that delivery stories can be drafted from it with `requirements-to-stories`.

Done when the frozen set is delivered and every item reads `published`.


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

# Included file: references/page-format.md

````markdown
# Page format

Authored here, not generated from `shared/`. The page is plain markdown so that a future connector can publish the same content unchanged.

## Title

`<CODE> <Set name>`, e.g. `IMT Incident logging and prioritisation`.

## Part 1: page properties

Goes inside Confluence's Page Properties macro, so Confluence can build a requirements catalogue across initiatives.

| Field | Value |
|---|---|
| Initiative code | <CODE> |
| Set name | <Set name> |
| Version | <set version> |
| Status | Awaiting approval |
| Business analyst | <BA name> |
| Validated by | <from the set header> |
| Validated on | <from the set header> |
| AI use | <proposed page label> |
| Workspace file | requirements/<set-slug>.md |

## Part 2: body

1. One `## <Class name>` section per class present, in the order BR, SR, FR, NFR, TR.
2. Per item, `### <ID> <statement>` and a trimmed table, in this order: Class · Rationale · Threshold · Priority · Source · Traces to · Reused from · AI use. Leave out Threshold and Reused from when they read `—`, and Priority while it reads `TBD`. Status and reviewer fields are never shown.
3. `## Open questions`: only the questions whose `Answered by` reads `—`, with columns #, Question, Findings involved, Ask. Leave the section out when none remain.
4. The footer line from `references/ai-use.md`.

## Page label

Propose `ai-generated` if any item is AI-generated, otherwise `ai-assisted` (`references/ai-use.md`). The BA decides.

## Pasting into Confluence Data Center

1. Create the page with the title above.
2. Insert the **Page Properties** macro. Inside it, use **Insert → Markup**, choose **Markdown**, and paste Part 1.
3. Below the macro, use **Insert → Markup → Markdown** again and paste Part 2.
4. Add the page label the BA chose.
5. Publish the page and send it for approval.
````

---

# Included file: references/requirement-set.md

````markdown
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
   | Validated by | <stakeholder roles, filled by the BA> |
   | Validated on | <YYYY-MM-DD, filled by the BA> |
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
- **Traces to**: SR, FR, NFR and TR trace to at least one BR; an FR may also trace to the SR it satisfies. A BR traces to `Business need`, and may also trace to the gaps (`GP`) it closes. Any item may also trace to the business rules (`RL`) or use cases (`UC`) it serves.
- **Status** values, in order: `draft`, `verified`, `validated`, `published`, `approved`, then `retired` or `superseded`. Only the BA sets `validated`, by hand, after filling `Validated by` and `Validated on` in the set header.

## Open questions

A table at the end of the set:

| # | Question | Findings involved | Ask | Answered by |
|---|---|---|---|---|
| 1 | <conflict, gap or missing rationale or threshold> | <finding IDs> | <stakeholder role> | — |

Conflicts between findings are listed here and never resolved by a skill. `Answered by` holds the confirmed finding IDs that answer the question, filled by `findings-to-requirements` when it uses them; the question row itself is never changed or removed.

## Changing a set

- A **draft** set may gain new items and open questions appended at the end of their sections. Each change raises the version by 0.1.
- Existing items are edited by one skill only, `check-requirement-quality`, in two ways, each item by each item with the BA's explicit approval: applying a rewrite the BA picked, and setting `Status`, `Reviewer` and `Reviewed on` when the BA confirms `verified`. No skill removes an item.
- `findings-to-requirements` fills an open question's `Answered by` when it uses a confirmed finding that answers it.
- `prepare-for-publication` makes one edit, after the BA confirms the page is live and gives its link: set Status `published` on the set and every item, and fill `Confluence page`. From then on the file is a frozen copy.
- A **published** set is a frozen copy: never changed. New needs go into a new set.
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

# Included file: templates/confluence-page.md

````markdown
**Page title:** <CODE> <Set name>
**Proposed page label:** <ai-generated / ai-assisted>

**Part 1: paste inside the Page Properties macro**

| Field | Value |
|---|---|
| Initiative code | <CODE> |
| Set name | <Set name> |
| Version | <version> |
| Status | Awaiting approval |
| Business analyst | <BA name> |
| Validated by | <roles> |
| Validated on | <YYYY-MM-DD> |
| AI use | <proposed page label> |
| Workspace file | requirements/<set-slug>.md |

**Part 2: paste below the macro**

## <Class name>

### <ID> <statement>

| Field | Value |
|---|---|
| Class | <class> |
| Rationale | <rationale> |
| Threshold | <threshold> |
| Source | <sources> |
| Traces to | <IDs> |
| AI use | <label> |

## Open questions

| # | Question | Findings involved | Ask |
|---|---|---|---|

---
Produced with prepare-for-publication v<version> in <runtime>, <YYYY-MM-DD>.
````
