# Evals: check-requirement-quality

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/` with `reviews/` emptied. The example report in `reviews/` is a reference answer for case 1.

## 1. Check the example sets

- **Runtime:** Claude Code.
- **Prompt:** "Check the quality of the incident logging set."
- **Checks:**
  - [ ] Reads `business-requirements.md` with the set without being told.
  - [ ] Writes `reviews/incident-logging-and-prioritisation-quality-<date>.md` with a result in every column for all seven items.
  - [ ] Prioritised reads `pending` for every item; M and T read `n/a` for SR and FR.
  - [ ] Must fix: Measurable and Time-bound on both BRs; Unambiguous on IMT-SR-001 and IMT-FR-003; Complete and Measurable on IMT-NFR-001.
  - [ ] Flags the IMT-NFR-001 → IMT-BR-001 trace as unsupported (⚠).
  - [ ] Suggested rewrites invent no number or date; they say whom to ask.
  - [ ] Each rewrite is marked wording only or substance.
  - [ ] Proposes only IMT-FR-001 and IMT-FR-002 as verified.
  - [ ] Changes no set file before the BA answers.

## 2. Confirm verified

- **Continue case 1, reply:** "Confirm FR-001 and FR-002 as verified. No rewrites."
- **Checks:**
  - [ ] Those two items get `Status: verified`, `Reviewer: Alex Rivera`, `Reviewed on: <today>`.
  - [ ] The logging set's version becomes 0.2; `business-requirements.md` is unchanged.
  - [ ] Every other item is unchanged.

## 3. Apply rewrites

- **Continue case 1, reply:** "Apply rewrite 7 with a warning period of 30 minutes."
- **Checks:**
  - [ ] IMT-SR-001's statement now names the 30-minute warning period; its AI use is unchanged (wording only).
  - [ ] No other item changes, and the version rises once.

## 4. Vague and compound wording

- **Runtime:** any. Add to the logging set: `### IMT-FR-004 The system shall be user-friendly and log and assign incidents quickly.` with a complete item table.
- **Prompt:** "Check the logging set."
- **Checks:**
  - [ ] IMT-FR-004 fails Atomic and Unambiguous (✗), naming "user-friendly" and "quickly".
  - [ ] The suggested rewrite splits it into separate requirements.

## 5. Published set

- **Runtime:** Claude Code, with the logging set's status changed to `published`.
- **Prompt:** "Check the logging set."
- **Checks:**
  - [ ] Declines to check or change it, explaining it is a frozen copy.

## 6. Missing finding

- **Runtime:** any. Change IMT-FR-002's Source to `IMT-FN-099`.
- **Prompt:** "Check the logging set."
- **Checks:**
  - [ ] IMT-FR-002 fails Structure (✗): the finding does not exist.
