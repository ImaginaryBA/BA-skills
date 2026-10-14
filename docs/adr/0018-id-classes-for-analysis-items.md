# Analysis items that others trace to get IDs; the rest are labelled rows

Some analysis items are referenced from elsewhere: requirements address gaps and enforce business rules, options address gaps and carry risks, stories follow use cases, the business case weighs options and risks. These get IDs from the initiative's ID register (ADR 0008), with five new classes: `GP` gap, `RK` risk, `OP` design option, `RL` business rule, `UC` use case. They are written as `### <ID> <statement>` headings with an item table, like requirements.

Everything else in an analysis (SWOT entries, PESTLE factors, five-forces entries, current-state observations, process steps, data entities) is a row in a table without an ID. Each row still carries its own Evidence and AI use label (ADR 0004), as findings do. We rejected IDs on every row because nothing traces to a SWOT entry, and hundreds of IDs would bury the ones that matter.

Requirements keep citing findings in `Source`. Their `Traces to` may now also cite `GP`, `RL` and `UC` IDs, so a business requirement can show the gap it closes. A missing class row in an older initiative's ID register reads as `000`, and the first skill to use the class adds the row.
