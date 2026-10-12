---
name: requirements-to-stories
description: "Draft delivery stories with Gherkin acceptance criteria from validated requirements, check them against INVEST, give Jira Data Center copy-and-paste blocks, and later record each story's Jira key. Use when requirements are validated and the delivery team needs Jira stories."
---

<!-- Generated from skills/requirements-to-stories/ (v0.1.0) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Requirements to stories

Turns validated requirements into stories a delivery team can build and test. Every story traces to requirements, every criterion to what the requirements say. Two modes: **Draft** and **Record keys**.

References (read before step 1): `references/story-format.md`, `references/requirement-set.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## Draft

### 1. Load

Read `INITIATIVE.md`, `stakeholders.md`, the requirement set the BA names, `business-requirements.md` and any existing story set for it; run the clearance check and read the ID register. In a chat runtime, ask for these and wait.

- Items not yet `validated` (or later) are left out; list them.
- If the set's status is `published`, it is a frozen copy: ask the BA to confirm nothing changed in Confluence since publication, and wait for the answer.

Done when the eligible items are known and, for a frozen copy, the BA has confirmed.

### 2. Propose, then wait

Show the BA the planned stories: short title, role, `Derived from`, and where each NFR lands (as criteria on which stories, or its own story). Wait for the BA to confirm or change it. Write nothing before that.

Done when the BA has confirmed the plan.

### 3. Write

Fill `templates/story-set.md` per `references/story-format.md`: new ST IDs from the register, `Status: draft`, `AI use: AI-generated`, reviewer fields empty, at least one Gherkin scenario each. Extending an existing story set: append only, raise its version by 0.1. Then check every story against INVEST.

Done when every confirmed story is written with all fields and criteria, and every INVEST failure is listed.

### 4. Deliver

Deliver the story set and updated ID register per `references/workspace.md`. Then show:
- one Jira Data Center block per story (`references/story-format.md`);
- INVEST failures with suggested fixes, and every `TBD` carried into criteria;
- the items left out and why.

Ask the BA to review the stories; when the BA confirms a story is reviewed, set `Status: ready`, `Reviewer` (the BA) and `Reviewed on` (today). Next step: create the ready stories in Jira, then report their keys.

Done when the BA has the file, the blocks and the lists.

## Record keys

When the BA reports Jira keys (e.g. "IMT-ST-003 is SD-431"): fill `Jira key` and set `Status: created` for exactly those stories, and change nothing else. Deliver the file.

Done when every reported key is recorded.


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

# Included file: references/ids.md

````markdown
# IDs

## Format

`<CODE>-<CLASS>-<NNN>`, e.g. `IMT-FR-012`.

- `CODE`: the initiative code, 2–5 uppercase letters.
- `CLASS`: `BR` business, `SR` stakeholder, `FR` functional, `NFR` non-functional, `TR` transition requirement; `ST` delivery story (temporary until its Jira key is recorded); `FN` elicitation finding.
- `NNN`: sequence within the initiative and class, zero-padded to 3 digits, starting at 001.

IDs are never renumbered or reused. A retired or superseded item keeps its ID. An item copied from another initiative gets a new ID plus a `Reused from` value naming the original.

## ID register

The ID register is a table in `INITIATIVE.md` holding the last number used per class. It is the source of every new ID.

1. Read the register. Next ID = last used + 1.
2. In an agentic runtime, also scan `elicitation/`, `requirements/` and `stories/` for the highest number per class. If the scan finds a higher number than the register, stop and show the BA both numbers; continue only once the BA says which is right.
3. After creating IDs, output the updated register (in a chat runtime, as an updated `INITIATIVE.md` block).
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
- **Traces to**: SR, FR, NFR and TR trace to at least one BR; an FR may also trace to the SR it satisfies. A BR traces to `Business need`.
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

# Included file: references/story-format.md

````markdown
# Story format

Authored here, not generated from `shared/`.

## Story set file

One file in `stories/` per requirement set, with the same slug (`stories/incident-logging-and-prioritisation.md`). Header table: Set name · Initiative code · Version · Business analyst · Requirement set (path and version it was drafted from).

## Each story

`### <ST ID> <short title>`, then the statement, an item table, and acceptance criteria.

**Statement:** As a `<story role>`, I want `<capability>`, so that `<benefit, from the requirement's rationale>`. A story role is a role from `stakeholders.md` or a user role defined in the initiative glossary; when the right user role is missing, propose a glossary entry for the BA to confirm.

| Field | Value |
|---|---|
| Status | draft / ready / created |
| Derived from | <requirement IDs> |
| Jira key | TBD |
| AI use | AI-generated / AI-assisted |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: <name>
  Given <context>
  When <action>
  Then <observable result>
```

At least one scenario per story. Use only values the requirements give (thresholds included); a value the requirements leave `TBD` stays `TBD` in the scenario and is listed for the BA.

## Mapping requirements to stories

- **FR**: one or more stories each; split when a story would fail Small.
- **NFR**: acceptance criteria on the stories it constrains; its own story only when no story covers it.
- **TR**: its own stories.
- **BR, SR**: never directly; they are reached through `Derived from` traces.

## INVEST

Check every story: Independent · Negotiable · Valuable · Estimable · Small · Testable. List each failure for the BA with a suggested fix; never drop a story silently.

## Statuses

- `draft`: as drafted.
- `ready`: the BA has reviewed it; `Reviewer` and `Reviewed on` filled.
- `created`: the BA has created it in Jira and reported its key.

## Jira Data Center output

One block per story, for copy and paste, description in Jira wiki markup:

```
Summary: <short title>
Labels: <ai-generated or ai-assisted> <each Derived from ID>

Description:
h3. User story
As a <role>, I want <capability>, so that <benefit>.

h3. Acceptance criteria
{noformat}
Scenario: <name>
  Given <context>
  When <action>
  Then <observable result>
{noformat}

h3. Traceability
* Derived from: <IDs>, <Confluence page link if the set is published>
* Story: <ST ID> in stories/<slug>.md

Produced with requirements-to-stories v<version> in <runtime>, <YYYY-MM-DD>.
```
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

# Included file: templates/story-set.md

````markdown
# <Set name>: stories

| Field | Value |
|---|---|
| Set name | <Set name> |
| Initiative code | <CODE> |
| Version | 0.1 |
| Business analyst | <BA name> |
| Requirement set | requirements/<set-slug>.md v<version> |

### <ST ID> <short title>

**Statement:** As a <role>, I want <capability>, so that <benefit>.

| Field | Value |
|---|---|
| Status | draft |
| Derived from | <IDs> |
| Jira key | TBD |
| AI use | AI-generated |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: <name>
  Given <context>
  When <action>
  Then <observable result>
```

---
Produced with requirements-to-stories v<version> in <runtime>, <YYYY-MM-DD>.
````
