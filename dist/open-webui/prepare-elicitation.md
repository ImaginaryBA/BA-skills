---
name: prepare-elicitation
description: "Prepare an interview guide (30-minute sessions, split across several when needed) or a questionnaire for named stakeholders, covering the BA's goals and the open questions those stakeholders can answer, with the mandatory AI disclosure. Use before talking to or surveying stakeholders."
---

<!-- Generated from skills/prepare-elicitation/ (v0.1.1) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Prepare elicitation

Builds what the BA takes into an interview or sends out as a questionnaire. The guide works for the BA in the room: short, neutral questions with probes, time boxes that add up to 30 minutes, and the open questions that are waiting on these people.

References (read before step 1): `references/question-craft.md`, `references/ai-use.md`, `references/findings.md`, `references/requirement-set.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Collect the inputs

Read `INITIATIVE.md` and `stakeholders.md` and run the clearance check. In a chat runtime, ask for them, plus any draft requirement sets, and wait.

Needed from the BA: technique (interview or questionnaire) · participants (named from the register) · goals · date, if known. Ask for whatever is missing in one message, then wait.

A participant missing from the register is added as `references/workspace.md` describes.

Done when technique, participants and goals are known and every participant is in the register.

## 2. Gather what to cover

- The BA's goals.
- Every open question in draft requirement sets (including `business-requirements.md`) whose `Ask` names a participant's role and whose `Answered by` reads `—`.
- Every row in a `## Questions for stakeholders` section (from `grill-ba`) whose `Ask` names a participant's role.
- Gaps: list each approver and each high-influence stakeholder in the register who is not a participant and appears in no earlier elicitation file. Show these to the BA as a warning that does not block: carry on, and repeat the gaps at delivery so the BA can decide.

Done when every goal and matching open question is listed, and the gaps are shown.

## 3. Build

Follow `references/question-craft.md` and fill `templates/interview.md` or `templates/questionnaire.md`:
- participants as roles, never names;
- the AI disclosure from `references/ai-use.md`, word for word;
- every listed goal and open question covered by at least one question, each open question marked with its reference.

Interviews: when the content does not fit one 30-minute session, split it into several sessions, one file each, numbered `Session 1 of N`.

Done when every goal and open question appears in a guide or questionnaire, every interview's time boxes add up to 30 minutes, and every questionnaire has 15 questions or fewer (or the BA has accepted the warning).

## 4. Deliver

Deliver each file as `elicitation/<YYYY-MM-DD or undated>-<slug>.md` per `references/workspace.md`. Then tell the BA:
- which open questions each session or questionnaire covers;
- the gaps from step 2;
- next step: after the session, paste the notes or transcript into the file's `## Notes` section and run `notes-to-findings`.

Done when the BA has every file and both lists.


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

# Included file: references/question-craft.md

````markdown
# Question craft

Authored here, not generated from `shared/`.

## Every question

- Asks one thing.
- Is neutral: no assumed answer ("Don't you think…"), no proposed solution ("Would automatic assignment help?").
- Uses the initiative glossary's terms.
- Names no other stakeholder; refer to roles.

## Interview guide (30 minutes)

| Part | Minutes | Content |
|---|---|---|
| Opening | 3 | Purpose of the session, how notes are taken, the AI disclosure |
| Context | 4 | The participant's role and current way of working |
| Topics | 19 | 2–3 topics; per topic 2–4 open questions, each with 1–2 follow-up probes and a time box |
| Closing | 4 | Recap, how findings will be confirmed with them, next steps |

Open questions from requirement sets go into the topic they belong to, each marked with its reference (e.g. `incident-logging-and-prioritisation OQ 2`).

When the topics do not fit in 19 minutes, split them across sessions of 30 minutes each, every session with its own opening, context and closing, ordered so that open questions on business requirements come first, then the rest in the order of the goals.

## Questionnaire

- Introduction: purpose, how long it takes, the AI disclosure, the reply deadline.
- At most 15 questions (about 10 minutes); warn the BA above that.
- Each question states its type: single choice, multiple choice, agreement scale (5 points, Strongly disagree to Strongly agree), or free text; its options; and whether it is required.
- Choice options do not overlap and include "Other" or "Not applicable" where an answer might not fit.
- Plain markdown, so the BA can paste it into Confluence or an email.
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

# Included file: templates/interview.md

````markdown
# <Session title>

| Field | Value |
|---|---|
| Source | Interview |
| Date | <YYYY-MM-DD or TBD> |
| Session | <n> of <total> |
| Duration | 30 minutes |
| Participants | <roles> |

## Plan

**Goals**
- <goal>

**Open questions to resolve**

| Reference | Question |
|---|---|

## Interview guide

### Opening (3 min)
- <purpose>
- <how notes are taken>
- AI disclosure: "<wording from references/ai-use.md>"

### Context (4 min)
1. <question>
   - Probe: <follow-up>

### <Topic> (<n> min)
1. <question> <(resolves reference)>
   - Probe: <follow-up>

### Closing (4 min)
- <recap>
- <how findings will be confirmed>
- <next steps>

---
Produced with prepare-elicitation v<version> in <runtime>, <YYYY-MM-DD>.
````

---

# Included file: templates/questionnaire.md

````markdown
# <Questionnaire title>

| Field | Value |
|---|---|
| Source | Questionnaire |
| Date | <send date or TBD> |
| Reply by | <date or TBD> |
| Participants | <roles> |

## Plan

**Goals**
- <goal>

**Open questions to resolve**

| Reference | Question |
|---|---|

## Questionnaire

**Introduction**

<purpose> This takes about <n> minutes. Please reply by <date>.

<AI disclosure wording from references/ai-use.md>

**1. <question>** <(resolves reference)>
Type: <single choice / multiple choice / agreement scale / free text> · Required: <yes/no>
- <option>

---
Produced with prepare-elicitation v<version> in <runtime>, <YYYY-MM-DD>.
````
