---
name: grill-ba
description: "Question the BA relentlessly, in rounds, about a vague business need until its problem, cause, people affected, outcome, measures, scope edges, constraints, risks and decision makers are clear or known to be unknown. Records the BA's answers as unconfirmed findings and the unknowns as questions for stakeholders. Use when a need is fuzzy, before planning elicitation."
---

<!-- Generated from skills/grill-ba/ (v0.1.0) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Grill the BA

Interviews the BA, not a stakeholder. The aim is to surface what the BA assumes, what nobody knows yet, and whom to ask. Every answer is the BA's understanding; only a stakeholder can confirm it.

References (read before step 1): `references/findings.md`, `references/ids.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load

Read `INITIATIVE.md`, `stakeholders.md` and existing elicitation files; run the clearance check and read the ID register. In a chat runtime, ask for them and wait. Ask the BA which need to sharpen, if not given.

Done when the need is named and the workspace files are loaded.

## 2. Grill in rounds

Work through these topics, deepening each answer: **problem** (what happens today, how often) · **cause** (why it happens) · **affected** (who, how badly) · **outcome** (what changes when solved) · **measure** (how success shows, in numbers) · **scope edges** (what is in, what is out) · **constraints** (time, money, rules, systems) · **risks and assumptions** · **decision makers** (who decides, who approves).

Each round, ask every question you can ask now, numbered, then wait. A question whose answer depends on another unanswered question waits for a later round. Skip what `INITIATIVE.md` or confirmed findings already answer.

- Ask about the business; never suggest an answer to it.
- For process questions only ("who should we ask about this?"), you may suggest an answer from the register, marked **AI-suggested**.
- The BA may answer, say **unknown**, or say **stop**. Each unknown becomes a question for stakeholders, with the register role to ask.
- Names the BA mentions become roles.

Done when every topic is answered or marked unknown with a role to ask, or the BA says stop.

## 3. Record

Write a new elicitation file, `elicitation/<YYYY-MM-DD>-grilling-<slug>.md`, per `references/findings.md`:
- header: Source `Grilling`, Participants `Business analyst`;
- `## Notes`: the BA's answers, by topic;
- `## Findings`: one row per answer statement, Stakeholder role `Business analyst`, `Confirmed: no`, `AI use: AI-assisted` (the BA supplied the substance), `Answers` `—`;
- `## Questions for stakeholders`: every unknown, with the role to ask and its topic.

Deliver the file and the updated ID register per `references/workspace.md`. Tell the BA that these findings become requirements only after a stakeholder confirms them, and suggest `prepare-elicitation` to put the questions to the right people.

Done when the file holds every answer and every unknown, and the BA has it.


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

# Included file: references/findings.md

````markdown
# Findings

A finding is one statement from elicitation, attributed to a stakeholder role. Every requirement's `Source` is one or more finding IDs.

## Elicitation file

One file per session or source document in `elicitation/`, named `<YYYY-MM-DD>-<slug>.md` (e.g. `2026-10-12-service-desk-workshop.md`). It starts with a header table (Source, Date, Participants as roles) and grows through the session's life, each section added by the skill that owns it:

1. `## Plan` and `## Interview guide` or `## Questionnaire`: `prepare-elicitation`.
2. `## Notes`: cleaned notes written by `notes-to-findings` from what the BA pasted in the chat. Raw notes and transcripts are never saved: names become roles and small talk is dropped, content is kept.
3. `## Findings`: the findings table below.

A file from `grill-ba` has Source `Grilling`, `## Notes`, `## Findings` and `## Questions for stakeholders` (columns #, Question, Ask, Topic).

A file made from raw input or a workshop may hold only the header and `## Findings`.

| ID | Finding | Stakeholder role | Confirmed (yes/no) | AI use | Answers |
|---|---|---|---|---|---|
| IMT-FN-004 | Agents re-key critical monitoring alerts into the ticketing tool by hand. | Service Desk Lead | yes | AI-generated | — |

- **ID**: from the ID register, class `FN` (`references/ids.md`).
- **Finding**: one statement, in the stakeholder's meaning, without names (`references/data-classification.md`).
- **Stakeholder role**: as written in `stakeholders.md`, or `Business analyst` for the BA's own understanding (from `grill-ba`); those findings need a stakeholder's confirmation like any other.
- **Confirmed**: `yes` only when the stakeholder has confirmed the BA's understanding of it.
- **AI use**: per `references/ai-use.md`.
- **Answers**: the open question this finding answers (e.g. `incident-logging-and-prioritisation OQ 2`), or `—`.

Only confirmed findings become requirements. Unconfirmed findings become open questions.

`Confirmed` changes from `no` to `yes` only when the BA reports that the stakeholder confirmed it, and only `notes-to-findings` makes that change. A finding the stakeholder corrects stays `no`; the corrected statement becomes a new finding.
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
