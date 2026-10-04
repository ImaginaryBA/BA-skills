# Workspaces declare a data classification; personal data is pseudonymised

Internal business information may be processed by any runtime cleared under the company's AI agreements; customer and production data may not. Each workspace declares its data classification once, each skill declares which runtimes are cleared for it, and skills that ingest notes or transcripts flag personal data and offer to replace names with roles. This is a compliance constraint that is invisible in the skills themselves, so it is recorded here.

Confluence content is a special case: only local models may process it, so no skill takes Confluence pages as input in any other runtime (see ADR 0009).
