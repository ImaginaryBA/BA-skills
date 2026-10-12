---
name: set-up-initiative
description: "Start the workspace for a new initiative — creates INITIATIVE.md (business need, scope, glossary, data classification, cleared runtimes, initiative code, ID register), the stakeholder register and the empty folders. Use when a BA begins a new piece of analysis work, or when another skill finds no INITIATIVE.md."
---

<!-- Generated from skills/set-up-initiative/ (v0.1.0) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Set up an initiative

Creates a new workspace exactly as the BA describes it. The BA's facts are the only source: every field holds what the BA said or is marked `TBD`.

References (read before step 1): `references/workspace.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`.

## 1. Collect the inputs

Mandatory: initiative name · initiative code · business need (2–5 sentences) · scope in · scope out · data classification · runtimes cleared for that classification · the BA's name.
Optional: sponsor · initial stakeholders (any register columns the BA knows) · known terms with definitions.

Take what the BA has already given. Ask for **all** missing mandatory inputs in a single message, then wait. Optional inputs the BA leaves out become `TBD`.

Checks before going on:
- Code is 2–5 uppercase letters. If it matches a common ticket prefix (`INC`, `REQ`, `CHG`, `PRB`, `TASK`, `RITM`), point out the clash and ask the BA to confirm or choose another.
- Classification is one of the four levels.
- The current runtime is in the BA's cleared list (`references/data-classification.md`). If not, stop and say why.
- In an agentic runtime, no `INITIATIVE.md` already exists in the target folder. If one does, stop: this skill never overwrites a workspace.

Done when every mandatory input has a value the BA supplied and all four checks pass.

## 2. Build the files

Fill `templates/INITIATIVE.md` and `templates/stakeholders.md`.

- Keep the BA's wording for business need and scope; correct spelling and grammar only.
- Stakeholder names stay as given (the register keeps real names).
- Glossary: only terms the BA supplied. Leave the table with its header row if there are none.
- ID register: every class at `000`.
- End each file with the footer from `references/ai-use.md`; workspace files carry no other provenance.

Done when no placeholder in angle brackets remains: every field is filled from the BA's input or reads `TBD`.

## 3. Deliver

Deliver the two files and the empty folders `elicitation/`, `requirements/`, `stories/`, `decisions/`, `reviews/` as `references/workspace.md` describes for this runtime. In a chat runtime, list the empty folders in the tree for the BA to create.

Then list every `TBD` field and suggest the next step: prepare elicitation with `prepare-elicitation`, or, when the business need is still vague, sharpen it first with `grill-ba`.

Done when the BA has the complete folder tree and both files, and every `TBD` is listed.


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

# Included file: templates/INITIATIVE.md

````markdown
# <Initiative name> (<CODE>)

| Field | Value |
|---|---|
| Initiative code | <CODE> |
| Business analyst | <BA name> |
| Sponsor | <sponsor or TBD> |
| Data classification | <Public / Internal / Confidential / Restricted> |
| Cleared runtimes | <runtimes the company clears for this classification> |
| Created on | <YYYY-MM-DD> |

## Business need

<2–5 sentences, in the BA's words>

## Scope

**In scope**
- <item>

**Out of scope**
- <item>

## Glossary

| Term | Definition | Avoid |
|---|---|---|

## ID register

| Class | Meaning | Last used |
|---|---|---|
| BR | Business requirement | 000 |
| SR | Stakeholder requirement | 000 |
| FR | Functional requirement | 000 |
| NFR | Non-functional requirement | 000 |
| TR | Transition requirement | 000 |
| ST | Delivery story | 000 |
| FN | Elicitation finding | 000 |

---
Produced with set-up-initiative v<version> in <runtime>, <YYYY-MM-DD>.
````

---

# Included file: templates/stakeholders.md

````markdown
# Stakeholder register: <Initiative name> (<CODE>)

| Name | Role | Organisational unit | Interest (H/M/L) | Influence (H/M/L) | Approver (yes/no) | Preferred engagement | Notes |
|---|---|---|---|---|---|---|---|

---
Produced with set-up-initiative v<version> in <runtime>, <YYYY-MM-DD>.
````
