# Page format

Authored here, not generated from `shared/`. The page is plain markdown so that a future connector can publish the same content unchanged.

## Title

`<CODE> <Set name or Analysis name>`, e.g. `IMT Incident logging and prioritisation`, `IMT Current state`.

## Requirement set

### Part 1: page properties

Goes inside Confluence's Page Properties macro, so Confluence can build a requirements catalogue across initiatives.

| Field | Value |
|---|---|
| Initiative code | <CODE> |
| Set name | <Set name> |
| Version | <set version> |
| Status | Awaiting approval |
| Business analyst | <BA name> |
| Validated by | <from the set header> |
| Validated on | <from the set header> |
| AI use | <proposed page label> |
| Workspace file | requirements/<set-slug>.md |

### Part 2: body

1. One `## <Class name>` section per class present, in the order BR, SR, FR, NFR, TR.
2. Per item, `### <ID> <statement>` and a trimmed table, in this order: Class · Rationale · Threshold · Priority · Source · Traces to · Reused from · AI use. Leave out Threshold and Reused from when they read `—`, and Priority while it reads `TBD`. Status and reviewer fields are never shown.
3. Open questions, as below.
4. The footer line from `references/ai-use.md`.

## Analysis

### Part 1: page properties

| Field | Value |
|---|---|
| Initiative code | <CODE> |
| Analysis name | <Analysis name> |
| Kind | <kind from the header> |
| Version | <analysis version> |
| Status | Awaiting approval |
| Business analyst | <BA name> |
| Validated by | <from the header> |
| Validated on | <from the header> |
| Approver | <business case only: the Sponsor from `INITIATIVE.md`; leave the row out for other kinds> |
| AI use | <proposed page label> |
| Workspace file | analysis/<file name> |

### Part 2: body

1. Every section between the header table and `## Open questions`, in the file's order, with its headings and text unchanged.
2. Row tables: every column and row as in the file, except the `Reviewer` column, which is left out.
3. Items (`### <ID> <statement>`): every field in the file's order, except `Reviewer` and `Reviewed on`. Leave out fields reading `—`; keep fields reading `TBD`, because an open likelihood, impact or figure is something the approver must see.
4. Mermaid diagrams: the code block unchanged, then its element table.
5. Open questions, as below.
6. The footer line from `references/ai-use.md`.

## Open questions (both kinds)

`## Open questions`: only the questions whose `Answered by` reads `—`, with columns #, Question, Findings involved, Ask. Leave the section out when none remain.

## Page label

Propose `ai-generated` if any item or row on the page is AI-generated, otherwise `ai-assisted` (`references/ai-use.md`). The BA decides.

## Pasting into Confluence Data Center

1. Create the page with the title above.
2. Insert the **Page Properties** macro. Inside it, use **Insert → Markup**, choose **Markdown**, and paste Part 1.
3. Below the macro, use **Insert → Markup → Markdown** again and paste Part 2.
4. If Part 2 has a Mermaid code block: where the instance has a Mermaid macro, move the code into it; otherwise render the diagram with a tool the company allows and insert the image directly above the code block. Keep the code block and the element table either way: they are the checkable record.
5. Add the page label the BA chose.
6. Publish the page and send it for approval (for a business case, to the sponsor).
