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
