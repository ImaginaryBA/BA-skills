# Analyses are published like requirement sets

The business case needs the sponsor's approval, and strategy analyses are read by people who never open the workspace, so analyses are a second unit of publication alongside requirement sets (extending ADR 0007). The rules for requirement sets apply unchanged: the BA marks an analysis `validated` by hand after named stakeholders confirm it; `prepare-for-publication` produces the publish-ready page and proposes the `ai-generated` or `ai-assisted` page label; once the BA confirms the page is live, the workspace file is frozen (ADR 0009) and Confluence is master. Approval happens in Confluence (ADR 0010); for a business case the approver is the sponsor named in `INITIATIVE.md`.

Diagrams are Mermaid source in the workspace. Whether Confluence renders them depends on the company's instance; until that is confirmed, the publish-ready page carries the Mermaid source in a code block and tells the BA to paste a rendered image above it if no Mermaid macro is available.

`prepare-for-publication` must be extended to read analyses before any Phase 2 analysis can be published.
