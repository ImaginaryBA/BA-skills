# Evals: set-up-initiative

Run each case in a fresh session of the named runtime, with only this skill loaded. A case passes when every check holds. Record results per runtime; the skill is released once all cases pass in Claude Code and one other pilot runtime.

Shared input used by cases 1 and 3 (the BA's message):

> New initiative: Incident Management Ticketing, code IMT. Business need: [the "Business need" paragraph from `workspace-example/IMT-incident-management-ticketing/INITIATIVE.md`]. In scope: [its four in-scope bullets]. Out of scope: [its three out-of-scope bullets]. Classification Internal, cleared runtimes Claude Code, Codex, Open WebUI (local models). I'm Alex Rivera. Sponsor is the Head of IT Operations.

## 1. Complete input, agentic runtime

- **Runtime:** Claude Code, in an empty folder.
- **Prompt:** the shared input.
- **Checks:**
  - [ ] Creates `IMT-incident-management-ticketing/` with `INITIATIVE.md`, `stakeholders.md` and the five empty folders.
  - [ ] Business need and scope match the BA's wording (spelling and grammar fixes only).
  - [ ] ID register lists all seven classes at `000`.
  - [ ] Glossary and stakeholder tables contain only their header rows (none supplied).
  - [ ] No angle-bracket placeholder remains; anything not supplied reads `TBD`.
  - [ ] Each file ends with `Produced with set-up-initiative v0.1.0 in Claude Code, <today>.` and has no other AI use label.
  - [ ] Lists the `TBD` fields and suggests `prepare-elicitation`.

## 2. Missing mandatory inputs

- **Runtime:** any.
- **Prompt:** "Set up a new initiative for our incident ticketing replacement, code IMT."
- **Checks:**
  - [ ] Creates no files.
  - [ ] Asks, in one message, for: business need, scope in, scope out, data classification, cleared runtimes, the BA's name (and the initiative name, if it does not treat the description as the name).
  - [ ] Invents no value for any of them.

## 3. Chat runtime delivery

- **Runtime:** Open WebUI.
- **Prompt:** the shared input.
- **Checks:**
  - [ ] Prints the folder tree first, including the five empty folders.
  - [ ] Prints each file as its own block headed `Save as: <path>`, with complete content.
  - [ ] Footer names Open WebUI as the runtime.

## 4. Runtime not cleared

- **Runtime:** Codex.
- **Prompt:** the shared input, with cleared runtimes changed to "Claude Code only".
- **Checks:**
  - [ ] Stops before creating files and explains that Codex is not cleared for this classification.

## 5. Code clashes with a ticket prefix

- **Runtime:** any.
- **Prompt:** the shared input, with code `INC`.
- **Checks:**
  - [ ] Points out the clash with incident ticket numbers and asks the BA to confirm or choose another code before creating files.

## 6. Invalid code

- **Runtime:** any.
- **Prompt:** the shared input, with code `INCIDENTS`.
- **Checks:**
  - [ ] Asks for a 2–5 uppercase-letter code and creates no files.

## 7. Workspace already exists

- **Runtime:** Claude Code, in a folder that already holds `IMT-incident-management-ticketing/INITIATIVE.md`.
- **Prompt:** the shared input.
- **Checks:**
  - [ ] Overwrites nothing and says the workspace already exists.
