---
name: check-requirement-quality
description: "Check draft requirement sets against the BABOK quality characteristics, SMART, structure, traceability and vague wording; write a quality report with suggested rewrites; then apply the rewrites the BA picks and mark the items the BA confirms as verified. Use when a BA wants requirements reviewed, verified or made ready for stakeholder validation."
---

<!-- Generated from skills/check-requirement-quality/ (v0.1.1) by scripts/sync_shared.py. Edit the skill, not this file. -->

Every file this skill refers to, such as `references/<file>.md` or `templates/<file>.md`, is included in full at the end of this document under a heading with that path.

# Check requirement quality

Reviews requirements the way a demanding peer reviewer would: every item against every check in `references/checks.md`, every issue with a suggested rewrite. Edits happen only after the BA approves them, item by item.

References (read before step 1): `references/checks.md`, `references/requirement-set.md`, `references/findings.md`, `references/ai-use.md`, `references/data-classification.md`, `references/workspace.md`.

## 1. Load

Read `INITIATIVE.md` (glossary and business need) and run the clearance check. Ask the BA which draft sets to check, and check only those. Always read `requirements/business-requirements.md` alongside them for the trace checks (its items are checked only when the BA names it), and the elicitation files their items cite. A set with status `published` is a frozen copy: say so and leave it out. In a chat runtime, ask for these files and wait.

Done when the chosen draft sets, the business requirements and the cited findings are loaded.

## 2. Check every item

Run every check in `references/checks.md` on every item, and the cross-item checks (Consistent, duplicates, traceability) across all loaded sets. For each ✗ and ⚠, write the issue and a suggested rewrite. A rewrite uses only facts from the findings or the BA; where the fix needs a fact nobody has given (a number, a date), the rewrite says what to ask and whom, from the open questions. Mark each rewrite **wording only** (keeps the item's AI use) or **substance** (makes it AI-generated).

Done when every item has a result in every column and every ✗ and ⚠ has an issue row.

## 3. Report

Fill `templates/quality-report.md` and deliver it as `reviews/<set-slug>-quality-<YYYY-MM-DD>.md` (for several sets, use the first set's slug plus `-and-more`). Items with no ✗ are proposed as verified.

Then ask the BA, in one message: which rewrites to apply (by issue number), and which proposed items to confirm as verified. Wait. Change no set before the BA answers.

Done when the report is delivered and the BA has answered.

## 4. Apply what the BA approved

For each set touched, and nothing else:
- apply each approved rewrite; set AI use to `AI-generated` for substance rewrites, leave it for wording-only ones;
- for each confirmed item: `Status: verified`, `Reviewer:` the BA's name, `Reviewed on:` today;
- raise the set's version by 0.1, once per run;
- leave every other item exactly as it was.

Deliver the changed sets as `references/workspace.md` describes, and suggest the next step: validation with stakeholders, then `prepare-for-publication`.

Done when every approved change is in place, no unapproved change is, and the BA has the files.


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

# Included file: references/checks.md

````markdown
# Checks

Authored here, not generated from `shared/`. Every check yields one result per item: ✓ pass · ✗ must fix (blocks `verified`) · ⚠ consider · n/a · `pending` · `BA` (for the BA to judge).

## BABOK characteristics (BABOK v3 §7.2)

| Check | Passes when | Fails as |
|---|---|---|
| Atomic | One requirement per statement: no "and/or", no second "shall" | ✗ |
| Complete | Statement has no `TBD`; Rationale is not `TBD` | ✗ |
| Consistent | Contradicts no other item in the checked sets or `business-requirements.md`, and duplicates none | ✗ |
| Concise | States the need without explanation or solution design | ⚠ |
| Feasible | Not obviously impossible or self-contradictory; otherwise `BA` | ✗ when obvious, else `BA` |
| Unambiguous | One reading only: no vague term (below), no undefined qualifier ("at risk", "relevant"), no term the glossary says to avoid | ✗ |
| Testable | Someone could check it is met; BR and NFR need a Threshold | ✗ |
| Prioritised | Always `pending` until prioritisation (Phase 3) | `pending` |
| Understandable | Domain terms are in the initiative glossary or self-evident | ⚠ |

## SMART

| Check | BR, NFR | SR, FR, TR | Passes when | Fails as |
|---|---|---|---|---|
| Specific | yes | yes | Names who or what, and the condition | ✗ |
| Measurable | yes | n/a | Threshold holds a number or verifiable condition, not `TBD` | ✗ |
| Achievable | yes | yes | Nothing in the findings suggests it cannot be done | ⚠ |
| Relevant | yes | yes | BR traces to `Business need`; others trace to an existing BR | ✗ |
| Time-bound | yes | n/a | BR: says by when; NFR: says when or under which conditions the threshold applies (e.g. at peak load, from go-live) | BR ✗, NFR ⚠ |

## Structure

✗ when any of these fails: all eleven fields present · ID matches `<CODE>-<CLASS>-<NNN>` and its section's class · statement follows its class pattern · every Source is `Business need` or a finding ID that exists and is confirmed.

## Traceability

- ✗ SR, FR, NFR or TR with no trace to an existing BR.
- ⚠ A trace link no finding supports: neither item's sources state the need the link claims.
- ⚠ A BR that nothing traces to.

## Vague terms

fast, quick, slow, easy, simple, user-friendly, intuitive, flexible, robust, efficient, seamless, appropriate, adequate, sufficient, as needed, as appropriate, etc., and/or, minimal, maximal, optimal, state-of-the-art, support (as a verb without an object), handle.
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

# Included file: templates/quality-report.md

````markdown
# Quality report: <set name(s)>

| Field | Value |
|---|---|
| Initiative code | <CODE> |
| Sets checked | <file names and versions> |
| Checked on | <YYYY-MM-DD> |
| Items checked | <n> |
| Must fix | <n issues on n items> |
| Consider | <n> |
| Proposed as verified | <IDs> |

## Results

A = Atomic · Co = Complete · Cs = Consistent · Cn = Concise · F = Feasible · U = Unambiguous · Te = Testable · P = Prioritised · Un = Understandable · S M A R T · St = Structure · Tr = Traceability

| ID | A | Co | Cs | Cn | F | U | Te | P | Un | S | M | A | R | T | St | Tr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Issues

| # | ID | Check | Severity | Issue | Suggested rewrite | AI use after rewrite |
|---|---|---|---|---|---|---|

## Proposed as verified

<IDs with no must-fix issue, or "None.">

---
Produced with check-requirement-quality v<version> in <runtime>, <YYYY-MM-DD>.
````
