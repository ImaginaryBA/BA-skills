# Evals: ask-ba

Run each case in a fresh session of the named runtime, with only this skill loaded.

## 1. Status and next step

- **Runtime:** Claude Code, in a folder holding a copy of `workspace-example/`.
- **Prompt:** "Where am I with my initiative and what should I do next?"
- **Checks:**
  - [ ] Finds `IMT-incident-management-ticketing/INITIATIVE.md`, shows it, and asks the BA to confirm before reading further.
  - [ ] After confirmation, the summary says: two draft sets (2 BR items; 5 items in the logging set), findings IMT-FN-009 to 013 awaiting confirmation, and the open questions grouped by role (Head of IT Operations, Service Desk Lead, Information Security Officer).
  - [ ] Recommends one next step (e.g. `notes-to-findings` to confirm the interview findings, or `check-requirement-quality`) with a one-line reason.
  - [ ] Lists the workspace files that skill will use, for the BA to confirm.
  - [ ] Does not start running the recommended skill.

## 2. Chat runtime

- **Runtime:** Open WebUI, nothing attached.
- **Prompt:** "I've just finished a workshop with three stakeholders and have my notes."
- **Checks:**
  - [ ] Recommends `notes-to-findings` and lists the files to attach: `INITIATIVE.md`, `stakeholders.md`, the session's elicitation file, draft requirement sets.

## 3. Not covered

- **Runtime:** any.
- **Prompt:** "I need a SWOT analysis for the incident tool options."
- **Checks:**
  - [ ] Says BA-skills has no skill for this yet and points to coverage; does not produce a SWOT.

## 4. Coverage question

- **Runtime:** any.
- **Prompt:** "Which BABOK tasks does BA-skills cover?"
- **Checks:**
  - [ ] Answers from `references/coverage.md`, listing covered tasks with their skills and naming the knowledge areas with no coverage yet (Strategy Analysis, Solution Evaluation).

## 5. Changing a published set

- **Runtime:** any.
- **Prompt:** "The sponsor wants to change IMT-FR-002 but the set is already published."
- **Checks:**
  - [ ] Says changes to a published set are made in Confluence by hand and no skill touches it.
