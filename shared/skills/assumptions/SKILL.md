---
name: "assumptions"
description: "Surfaces the assumptions underneath something Claude said, or a doc, artifact or plan, and flags which are guesses. Use on /assumptions or \"what are you assuming\"."
---

# Assumptions

Dig under a statement, document, artifact or plan and lay out what it takes for granted, so the user can check the ground it stands on.

## Output format

**Examining:** [what is being examined, in one sentence]

| # | Assumption | Source | If wrong |
|---|------------|--------|----------|
| 1 | [what is taken for granted] | [User said, Evidence or Guess] | [what would change] |

**Riskiest:** [the assumption that would change the most if wrong, and why]

**Check:** [one concrete way to confirm or kill it]

## How to do this well

- Surface what is unstated; never just restate what the thing already says.
- Label the source honestly: "User said" only if they did, "Evidence" only if it can be pointed to, otherwise "Guess."
- Include assumptions about the user: their goal, audience, constraints and what "done" means.
- Order rows from most to least consequential, and keep only the ones that would change the outcome.
- Surface, don't fix; leave rewrites until the user asks.
- If it rests on Claude's own earlier guess, say so plainly.
- One sentence per cell; honest over diplomatic.