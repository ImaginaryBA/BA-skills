# Evals: prepare-for-publication

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/`.

**Validated setup** (cases 1–3): in `requirements/incident-logging-and-prioritisation.md`, set every item's Status to `validated`, `Validated by` to "Head of IT Operations, Service Desk Lead" and `Validated on` to 2026-10-20.

## 1. Build the page

- **Runtime:** Claude Code, validated setup.
- **Prompt:** "Prepare the incident logging set for Confluence."
- **Checks:**
  - [ ] Output matches `reference-page.md` in content: title, Part 1, Part 2 in class order, the unanswered open questions (four columns), footer.
  - [ ] Statements, rationale, thresholds and sources are copied word for word.
  - [ ] Threshold is left out where the set reads `—`; Priority is left out while `TBD`; no Status or reviewer rows appear.
  - [ ] Proposes the label `ai-generated` and says the BA decides.
  - [ ] Gives the Data Center paste steps (Page Properties macro, Insert → Markup → Markdown, label).
  - [ ] Writes no file and changes nothing in the workspace; asks for the page link.
  - [ ] Warns that IMT-BR-001 is not yet validated, without blocking.

## 2. Freeze after confirmation

- **Continue case 1, reply:** "Label confirmed. Page is live: https://confluence.example.com/display/IMT/Incident+logging"
- **Checks:**
  - [ ] Set header and every item read `published`.
  - [ ] `Confluence page` holds the link; the version is unchanged.
  - [ ] Nothing else in the file changed.
  - [ ] Says the file is now a frozen copy and suggests `requirements-to-stories`.

## 3. Chat runtime

- **Runtime:** Open WebUI, validated setup, with `INITIATIVE.md` and the set attached.
- **Prompt:** same as case 1.
- **Checks:**
  - [ ] Same page content as case 1; after the reply in case 2, prints the frozen set as one `Save as:` block.

## 4. Not validated

- **Runtime:** any, example as it is (items in `draft`).
- **Prompt:** same as case 1.
- **Checks:**
  - [ ] Refuses, listing every item that is not `validated` and the empty `Validated by` and `Validated on`.

## 5. Already published

- **Runtime:** any, with the set header's Status set to `published`.
- **Prompt:** same as case 1.
- **Checks:**
  - [ ] Stops, explaining the set is a frozen copy.

**Analysis setup** (cases 6–9): copy `fixtures/current-state.md` into the workspace as `analysis/current-state.md`.

## 6. Build an analysis page

- **Runtime:** Claude Code, analysis setup.
- **Prompt:** "Prepare the current state analysis for Confluence."
- **Checks:**
  - [ ] Output matches `reference-page-analysis.md` in content: title, analysis Part 1 (with Kind, without Approver), sections in file order (including Sources), the one unanswered open question, footer.
  - [ ] Rows, text and the Mermaid block are copied word for word; the `Reviewer` column is gone from both row tables.
  - [ ] Warns that the row "Agent assigns resolver group: by hand" rests on an assumption, without blocking.
  - [ ] Proposes `ai-generated` and says the BA decides.
  - [ ] The paste steps include the Mermaid step (macro, or rendered image above the code block, keeping the code and element table).
  - [ ] Writes no file and asks for the page link.

## 7. Freeze an analysis

- **Continue case 6, reply:** "Label confirmed. Page is live: https://confluence.example.com/display/IMT/Current+state"
- **Checks:**
  - [ ] Header Status reads `published`, `Confluence page` holds the link, the version stays 0.2.
  - [ ] A footer line is added below the two existing ones; nothing else changes (no Status added to rows).
  - [ ] Says the file is a frozen copy; does not suggest `requirements-to-stories`.

## 8. Analysis not validated

- **Runtime:** any, analysis setup with `Validated by` and `Validated on` emptied.
- **Prompt:** same as case 6.
- **Checks:**
  - [ ] Refuses, naming the two empty header fields; does not ask for item statuses.

## 9. Analysis already published

- **Runtime:** any, analysis setup with header Status `published`.
- **Prompt:** same as case 6.
- **Checks:**
  - [ ] Stops, explaining the analysis is a frozen copy.
