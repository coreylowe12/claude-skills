---
name: "why"
description: "Runs a 5 Whys root cause analysis on a mistake, failure or recurring problem, ending in one durable fix. Use on /why, \"why did X happen\" or \"what went wrong\"."
---

# 5 Whys

Chase a mistake or problem past the surface to its real cause, then name one fix that changes the default.

## Output format

**Problem:** [what went wrong, in one plain sentence]

| # | Why | Answer |
|---|-----|--------|
| 1 | Why did [problem]? | [answer] |
| 2 | Why did [answer 1]? | [answer] |
| 3 | Why did [answer 2]? | [answer] |
| 4 | Why did [answer 3]? | [answer] |
| 5 | Why did [answer 4]? | [answer] |

**Root cause:** [the last answer, stated as the underlying reason]

**Fix:** [one concrete, durable change to how things work]

## How to do this well

- Build each Why from the previous answer, not the original problem; the chain has to chain.
- Honest over diplomatic; if the real answer is "I padded it to look thorough," say that.
- The fix changes a default, a structure or a format; never "be more careful" or a reminder.
- One sentence per answer; the value is in the chain, not the prose.
- If the root cause is reached early, stop there and drop the empty rows rather than pad.