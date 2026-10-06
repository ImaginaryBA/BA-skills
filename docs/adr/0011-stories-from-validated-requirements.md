# Delivery stories may be created in Jira from validated requirements

Stories may be drafted and created in Jira as soon as their source requirements are `validated`, without waiting for approval in Confluence, so delivery isn't held up by sign-off. If a requirement later changes during approval, the BA amends it in Confluence and the affected stories in Jira by hand; the `derived_from` links show which stories to check.

Skills may draft stories from a frozen copy, because it is the BA's own workspace file and not Confluence content (ADR 0006). A frozen copy can lag behind Confluence edits, so a skill drafting from one says so in its output and asks the BA to confirm nothing changed in Confluence since publication.
