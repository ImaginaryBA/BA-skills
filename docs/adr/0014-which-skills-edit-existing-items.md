# Which skills may edit existing items, and only with the BA's approval

Skills append to draft requirement sets but never rewrite what is there, so the BA's reviewed wording cannot drift. The one exception is `check-requirement-quality`, which may make two kinds of edit, each approved item by item by the BA: applying a suggested rewrite the BA picked, and setting `Status: verified`, `Reviewer` and `Reviewed on` once the BA confirms. A rewrite that changes only wording keeps the item's AI use label; one that changes substance makes it AI-generated, and the skill states which applies before the BA approves. Every edit raises the set's version.

One further edit belongs to `prepare-for-publication`: once the BA confirms the page is live in Confluence and gives its link, it sets Status `published` on the set and every item and records the link, freezing the file. Done by hand this edit is easy to leave half-finished, and it marks the exact moment the file stops changing.
