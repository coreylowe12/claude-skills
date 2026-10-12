---
name: "lint"
description: "Checks the artifact or doc in a long session for anything stale against the latest decisions, fixes it in place, then lists the fixes. Use on /lint."
---

# Lint

Sweep the work in progress for anything the session has outgrown, fix it in place, and report what changed.

## Output format

**Checked:** [what was linted and the latest decisions it was checked against, in one sentence]

| # | Where | Stale | Fixed to |
|---|-------|-------|----------|
| 1 | [section, slide, row or line] | [what was out of date] | [what it says now] |

**Left alone:** [anything where the current version is unclear and needs the user's call, or "Nothing"]

**Result:** [the state of the work now, in one sentence]

## How to do this well

- Re-read the whole artifact or doc as it stands now; never lint from memory of an earlier version.
- The latest decision in the conversation is the source of truth; later beats earlier.
- Look for: contradictions with later decisions, outdated numbers, dates or names, references to removed parts, duplicates, leftover placeholders or TODOs, and terms or formatting used two ways.
- Fix in place before reporting; do not just list problems.
- Lint fixes staleness only; never add new content, restyle or restructure (that is /design-algorithm's job).
- If it is unclear which version is current, put it under Left alone instead of guessing.
- If nothing is stale, say so in Result and leave the table out rather than pad.
- One sentence per cell; honest over diplomatic.