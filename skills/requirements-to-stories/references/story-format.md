# Story format

Authored here, not generated from `shared/`.

## Story set file

One file in `stories/` per requirement set, with the same slug (`stories/incident-logging-and-prioritisation.md`). Header table: Set name · Initiative code · Version · Business analyst · Requirement set (path and version it was drafted from).

## Each story

`### <ST ID> <short title>`, then the statement, an item table, and acceptance criteria.

**Statement:** As a `<register role>`, I want `<capability>`, so that `<benefit, from the requirement's rationale>`.

| Field | Value |
|---|---|
| Status | draft / ready / created |
| Derived from | <requirement IDs> |
| Jira key | TBD |
| AI use | AI-generated / AI-assisted |
| Reviewer | |
| Reviewed on | |

**Acceptance criteria**

```gherkin
Scenario: <name>
  Given <context>
  When <action>
  Then <observable result>
```

At least one scenario per story. Use only values the requirements give (thresholds included); a value the requirements leave `TBD` stays `TBD` in the scenario and is listed for the BA.

## Mapping requirements to stories

- **FR**: one or more stories each; split when a story would fail Small.
- **NFR**: acceptance criteria on the stories it constrains; its own story only when no story covers it.
- **TR**: its own stories.
- **BR, SR**: never directly; they are reached through `Derived from` traces.

## INVEST

Check every story: Independent · Negotiable · Valuable · Estimable · Small · Testable. List each failure for the BA with a suggested fix; never drop a story silently.

## Statuses

- `draft`: as drafted.
- `ready`: the BA has reviewed it; `Reviewer` and `Reviewed on` filled.
- `created`: the BA has created it in Jira and reported its key.

## Jira Data Center output

One block per story, for copy and paste, description in Jira wiki markup:

```
Summary: <short title>
Labels: <ai-generated or ai-assisted> <each Derived from ID>

Description:
h3. User story
As a <role>, I want <capability>, so that <benefit>.

h3. Acceptance criteria
{noformat}
Scenario: <name>
  Given <context>
  When <action>
  Then <observable result>
{noformat}

h3. Traceability
* Derived from: <IDs>, <Confluence page link if the set is published>
* Story: <ST ID> in stories/<slug>.md

Produced with requirements-to-stories v<version> in <runtime>, <YYYY-MM-DD>.
```
