# Which skills may edit existing items, and only with the BA's approval

Skills append to draft requirement sets but never rewrite what is there, so the BA's reviewed wording cannot drift. Five skills have narrow exceptions. The first is `check-requirement-quality`, which may make two kinds of edit, each approved item by item by the BA: applying a suggested rewrite the BA picked, and setting `Status: verified`, `Reviewer` and `Reviewed on` once the BA confirms. A rewrite that changes only wording keeps the item's AI use label; one that changes substance makes it AI-generated, and the skill states which applies before the BA approves. Every edit raises the set's version.

A second belongs to `notes-to-findings`: it changes a finding's `Confirmed` value from `no` to `yes` exactly as the BA reports the stakeholder's confirmation, and nothing else.

A third belongs to `findings-to-requirements`: it fills an open question's `Answered by` with the confirmed finding that answers it, so answered questions stop looking open; the question itself is never changed or removed.

A fourth belongs to `prepare-for-publication`: once the BA confirms the page is live in Confluence and gives its link, it sets Status `published` on the set and every item and records the link, freezing the file. Done by hand this edit is easy to leave half-finished, and it marks the exact moment the file stops changing.

A fifth belongs to `requirements-to-stories`: on the BA's word it sets a story to `ready` with the BA as reviewer, and later records its Jira key and sets it to `created`; nothing else in the story changes.
