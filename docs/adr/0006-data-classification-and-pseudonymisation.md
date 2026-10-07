# Workspaces declare a data classification; names in elicitation content are replaced by roles

Internal business information may be processed by any runtime cleared under the company's AI agreements; customer and production data may not. The library uses generic classification levels (Public, Internal, Confidential, Restricted) and hardcodes no company runtime list: each workspace declares its classification and, per level, which runtimes the company clears, and skills check that declaration before working.

Skills that ingest notes or transcripts replace personal names with roles in elicitation notes and findings. The stakeholder register and the reviewer and approver fields keep real names, because accountability requires them; findings stay traceable to people through the register.

Confluence content is a special case: only local models may process it, so no skill takes Confluence pages as input in any other runtime (see ADR 0009).
