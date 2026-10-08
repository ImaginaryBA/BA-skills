# Evals: findings-to-requirements

Run each case in a fresh session of the named runtime, with only this skill loaded. Unless stated, start from a copy of `workspace-example/IMT-incident-management-ticketing/` with `requirements/` emptied and the ID register reset to `BR 000, SR 000, FR 000, NFR 000` (FN stays at `009`). The two files in the example's `requirements/` are a reference answer for case 1, not the only correct one.

## 1. Findings file, agentic runtime

- **Runtime:** Claude Code.
- **Prompt:** "Draft requirements from elicitation/2026-10-12-service-desk-workshop.md."
- **Checks before confirmation:**
  - [ ] Writes no file before the BA confirms.
  - [ ] Proposes sets with the findings going into each, the BRs to draft (flagged for BA and sponsor confirmation), and the open questions.
- **Then reply:** "Confirmed."
- **Checks after:**
  - [ ] BRs are in `requirements/business-requirements.md`, AI-generated, tracing to `Business need`.
  - [ ] IMT-FN-005 and IMT-FN-006 produce no requirement; their conflict is an open question.
  - [ ] IMT-FN-009 (unconfirmed) produces no requirement; it is an open question.
  - [ ] The NFR from IMT-FN-008 has Threshold `TBD` and an open question; no number is invented anywhere.
  - [ ] Every item has all eleven fields; status `draft`, priority `TBD`, reviewer fields empty.
  - [ ] Statements follow the class patterns; one requirement per statement.
  - [ ] Every SR, FR and NFR traces to at least one BR.
  - [ ] IDs start at 001 per class, and the updated ID register is delivered.
  - [ ] Each set ends with `## Open questions` and the footer.
  - [ ] Lists BRs awaiting confirmation and open questions by whom to ask, and suggests `check-requirement-quality`.

## 2. Raw input with names

- **Runtime:** any.
- **Prompt:** "Turn this into requirements: 'From: Sam Patel. Our agents waste time copying caller details from emails into tickets. Sam also says the portal should let users see their ticket status.'"
- **Checks:**
  - [ ] Creates a new elicitation file whose findings use `Service Desk Lead`, never "Sam Patel".
  - [ ] Labels the new findings AI-generated and asks which are confirmed by the stakeholder.
  - [ ] Turns unconfirmed findings into open questions, not requirements.

## 3. Extending a draft set

- **Runtime:** Claude Code, with the example's `requirements/` files and register left in place.
- **Prompt:** "Add this confirmed finding from the Service Desk Lead to the logging set: agents need to attach screenshots to incidents."
- **Checks:**
  - [ ] Appends a new item with ID `IMT-FR-004`; existing items are byte-for-byte unchanged.
  - [ ] Set version becomes 0.2.

## 4. Published set

- **Runtime:** Claude Code, with `incident-logging-and-prioritisation.md` set to status `published`.
- **Prompt:** same as case 3.
- **Checks:**
  - [ ] Leaves the published set unchanged and proposes a new set instead.

## 5. Register out of step

- **Runtime:** Claude Code, with the example's `requirements/` files in place but the register reset to `FR 000`.
- **Prompt:** same as case 3.
- **Checks:**
  - [ ] Stops, shows the register value and the highest scanned ID, and waits for the BA.

## 6. Chat runtime without the initiative file

- **Runtime:** Open WebUI.
- **Prompt:** the workshop file's findings table pasted alone.
- **Checks:**
  - [ ] Asks for `INITIATIVE.md` and `stakeholders.md` and writes nothing until they are attached.
