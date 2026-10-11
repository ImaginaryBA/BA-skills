# Page format

Authored here, not generated from `shared/`. The page is plain markdown so that a future connector can publish the same content unchanged.

## Title

`<CODE> <Set name>`, e.g. `IMT Incident logging and prioritisation`.

## Part 1: page properties

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

## Part 2: body

1. One `## <Class name>` section per class present, in the order BR, SR, FR, NFR, TR.
2. Per item, `### <ID> <statement>` and a trimmed table, in this order: Class · Rationale · Threshold · Priority · Source · Traces to · Reused from · AI use. Leave out Threshold and Reused from when they read `—`, and Priority while it reads `TBD`. Status and reviewer fields are never shown.
3. `## Open questions`, copied from the set, only when the set has any.
4. The footer line from `references/ai-use.md`.

## Page label

Propose `ai-generated` if any item is AI-generated, otherwise `ai-assisted` (`references/ai-use.md`). The BA decides.

## Pasting into Confluence Data Center

1. Create the page with the title above.
2. Insert the **Page Properties** macro. Inside it, use **Insert → Markup**, choose **Markdown**, and paste Part 1.
3. Below the macro, use **Insert → Markup → Markdown** again and paste Part 2.
4. Add the page label the BA chose.
5. Publish the page and send it for approval.
