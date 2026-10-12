# Evals: requirements-to-stories

Run each case in a fresh session of the named runtime, with only this skill loaded, on a copy of `workspace-example/IMT-incident-management-ticketing/`.

**Validated setup:** in `requirements/incident-logging-and-prioritisation.md`, set every item's Status to `validated` and fill `Validated by` and `Validated on`.

## 1. Draft from a validated set

- **Runtime:** Claude Code, validated setup.
- **Prompt:** "Draft stories for the incident logging set."
- **Checks before confirmation:**
  - [ ] Proposes the stories (title, role, Derived from) and where IMT-NFR-001 lands; writes nothing yet.
  - [ ] Proposes IMT-NFR-001 as its own story, since no story covers search.
- **Then reply:** "Confirmed."
- **Checks after:**
  - [ ] Writes `stories/incident-logging-and-prioritisation.md` matching `reference-stories.md` in structure and traces.
  - [ ] IDs start at `IMT-ST-001`; the updated ID register is delivered.
  - [ ] No story is derived from a BR or from IMT-SR-001 alone.
  - [ ] Every TBD from the requirements stays TBD in the criteria (warning period, search time, search rationale) and is listed; no number is invented.
  - [ ] One Jira Data Center block per story, in wiki markup (`h3.`, `{noformat}`), with labels `ai-generated` and the derived-from IDs.
  - [ ] Lists INVEST failures (e.g. IMT-ST-004 is not testable while its time is TBD).

## 2. Items not validated

- **Runtime:** any, example as it is (all items `draft`).
- **Prompt:** same as case 1.
- **Checks:**
  - [ ] Drafts nothing and lists every item that is not yet validated.

## 3. Frozen copy

- **Runtime:** Claude Code, validated setup, then the set's status set to `published` everywhere.
- **Prompt:** same as case 1.
- **Checks:**
  - [ ] Asks the BA to confirm nothing changed in Confluence since publication and waits before proposing stories.

## 4. Ready and record keys

- **Continue case 1, reply:** "ST-001 and ST-002 reviewed. ST-001 is SD-431."
- **Checks:**
  - [ ] IMT-ST-001 and IMT-ST-002 read `ready` with Reviewer Alex Rivera and today's date; then IMT-ST-001 reads `created` with Jira key `SD-431`.
  - [ ] Nothing else changes.

## 5. NFR as acceptance criteria

- **Runtime:** Claude Code, validated setup, with IMT-NFR-001 changed to "The system shall create an incident from a critical alert within 60 seconds of the alert" (Threshold "60 s"), tracing to IMT-BR-001.
- **Prompt:** same as case 1, then "Confirmed."
- **Checks:**
  - [ ] The 60-second limit becomes a scenario on the alert story (IMT-ST-001), not a separate story.
