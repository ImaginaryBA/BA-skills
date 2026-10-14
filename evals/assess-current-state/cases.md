# Evals: assess-current-state

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/` with `analysis/` emptied, unless stated. `workspace-example/IMT-incident-management-ticketing/analysis/current-state.md` is a reference answer for case 1, not the only correct one.

## 1. Findings only, agentic runtime

- **Runtime:** Claude Code.
- **Prompt:** "Assess the current state for IMT."
- **When asked for documents and capabilities, reply:** "No documents, no capabilities."
- **Checks before confirmation:**
  - [ ] Asks for documents and in-scope capabilities in one message; never asks to read a capability map.
  - [ ] Proposes `analysis/current-state.md`; offers SWOT; says PESTLE is available but lacks external documents; does not offer five forces.
  - [ ] Writes no file before the BA confirms.
- **Then reply:** "Confirmed, SWOT only."
- **Checks after:**
  - [ ] Header per `shared/analysis.md`: Kind `Current state`, version 0.1, status `draft`, validation fields empty.
  - [ ] Every row has Evidence and AI use `AI-generated`; `Reviewer` is empty everywhere.
  - [ ] Unconfirmed findings (e.g. IMT-FN-009, IMT-FN-011) are cited with `(unconfirmed)`; statements taken from the business need cite `Business need (unconfirmed)`.
  - [ ] No cause, figure or external fact appears that the findings or business need do not state; causes not given read `TBD` with an open question.
  - [ ] Baseline measures hold "about 5 minutes per alert" from IMT-FN-002 and nothing invented; missing figures read `TBD`, cite the evidence that makes them matter (not `Assumption`), and have open questions.
  - [ ] Findings about what the solution should do (IMT-FN-005, 006, 010, 013) are not rows; they are listed at delivery for `define-future-state`.
  - [ ] A "today" Mermaid flow of at most about eight steps, followed by its element table; any step without evidence is an `Assumption` with an open question.
  - [ ] SWOT opportunities are one row reading `No evidence yet.` with Evidence `—`, with suggested questions in open questions; no market or vendor claims.
  - [ ] No PESTLE or five-forces section; no `## Sources` section (no documents).
  - [ ] Ends with `## Open questions` (each with a register role) and the footer.
  - [ ] Delivery lists open questions by whom to ask and the count of rows on unconfirmed evidence or assumptions; suggests `prepare-elicitation`, then `define-future-state`.
  - [ ] Creates no IDs and leaves the ID register untouched.

## 2. Conflicting baseline figures

- **Runtime:** Claude Code, with `fixtures/service-desk-monthly-report-2026-09.md` copied into the workspace.
- **Prompt:** "Assess the current state for IMT. Use the September service desk report."
- **Reply to questions:** "No capabilities." then "Confirmed, SWOT only."
- **Checks:**
  - [ ] Two baseline rows for re-keying or logging an alert: about 5 minutes (IMT-FN-002) and 3 minutes (the report, by title and date); neither is dropped or averaged.
  - [ ] An open question names the conflict and asks which figure the business case should use.
  - [ ] The 11% breach share appears as a baseline with the report as evidence and Period September 2026.
  - [ ] `## Sources` lists the report with its date and owner role `Service Desk Lead`.

## 3. PESTLE without external documents

- **Runtime:** any.
- **Prompt:** "Assess the current state for IMT with a PESTLE analysis."
- **Reply to questions:** "No documents, no capabilities." then "Confirmed."
- **Checks:**
  - [ ] Explains that no supplied document covers external factors and lists questions that would feed PESTLE.
  - [ ] Writes no PESTLE entry with content; if the section exists, it reads `No evidence yet.`, and the questions are open questions.
  - [ ] Contains no regulatory, market or economic statement from the model's own knowledge.

## 4. Document with customer data

- **Runtime:** Claude Code, with both fixtures copied into the workspace.
- **Prompt:** "Assess the current state for IMT. Use the September report and the September incident export."
- **Checks:**
  - [ ] Sets the incident export aside, saying it holds customer data (customer names and emails), without repeating any of it.
  - [ ] Asks for a cleaned version and continues with the report.
  - [ ] No customer name, email or incident number from the export appears in the output.

## 5. Capabilities from the capability map

- **Runtime:** Claude Code.
- **Prompt:** "Assess the current state for IMT."
- **When asked, reply:** "No documents. Capabilities in scope: Incident management, Service level management, from the IT capability map v3, 2026-05-01. We also need alert correlation."
- **Checks:**
  - [ ] Does not ask for or try to read the capability map.
  - [ ] "Incident management" and "Service level management" appear under capabilities in scope, AI use `AI-assisted`, Evidence `IT capability map v3, 2026-05-01`.
  - [ ] "Alert correlation" is not added as a capability; it is an open question for the business architecture team.
  - [ ] Asking the business architecture team follows the workspace rule: the skill proposes a stakeholder row and appends it only after the BA confirms, or uses the role without adding it.
  - [ ] `## Sources` lists the capability map.

## 6. Extending a draft file

- **Runtime:** Claude Code, with the example's `analysis/current-state.md` in place, and a new confirmed finding IMT-FN-014 "Agents spend about 20 minutes a shift chasing resolver groups for updates." (Service Desk Lead) added to the interview elicitation file.
- **Prompt:** "Update the current state with the new finding."
- **Checks:**
  - [ ] Proposes extending `current-state.md`, not a new file.
  - [ ] Appends rows at the end of their sections (e.g. a problem and a baseline measure citing IMT-FN-014); every existing row is byte-for-byte unchanged.
  - [ ] Version becomes 0.2; a footer line is added below the existing one.

## 7. Published file

- **Runtime:** any, with the example's `analysis/current-state.md` in place and its Status set to `published`.
- **Prompt:** same as case 6.
- **Checks:**
  - [ ] Does not change `current-state.md`; explains it is a frozen copy.
  - [ ] Offers a separately scoped `current-state-<slug>.md` instead.

## 8. Chat runtime

- **Runtime:** Open WebUI, nothing attached.
- **Prompt:** "Assess the current state for IMT."
- **Checks:**
  - [ ] Asks for `INITIATIVE.md`, `stakeholders.md`, elicitation files and any current-state file, then stops.
- **Then attach** `INITIATIVE.md`, `stakeholders.md` and both elicitation files; reply as in case 1.
- **Checks:**
  - [ ] Prints the folder tree, then `analysis/current-state.md` as one `Save as:` block with the full file.
