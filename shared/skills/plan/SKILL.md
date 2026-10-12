---
name: "plan"
description: "Turns anything the user describes into a goal, then a short plan. Trigger on \"/plan\", \"let's plan\", \"give me a plan\", or \"how should we approach this\". Goal first, always."
---

# Plan

Name the real goal first, then lay out the fewest steps that get there. Plan only — don't start the work until the user says go.

## Output format

Always use this exact structure:

**Goal:** [one sentence — the outcome the user actually wants, not the activity]

**Done when:** [one sentence — the observable finish line]

| # | Step | Output |
|---|---|---|
| 1 | [action, verb first] | [what exists after this step] |
| 2 | [action] | [output] |
| 3 | [action] | [output] |

**First move:** [the single next action, small enough to do right now]

**Open question:** [only if something genuinely blocks the plan — otherwise omit this line]

## How to do this well

- The goal is the *why* behind the request, not a restatement of it. "Make a slide deck" is the activity; "get the budget approved" is the goal.
- If the goal is ambiguous, state your best read and plan from it. Don't stall with questions — The user can correct the goal in one line.
- Three to five steps, never more. Working memory holds about four things; a longer plan means the goal is too big — split it.
- Every step produces something concrete. If a step has no output, it's not a step.
- Name the trade-off or limit the user wouldn't see coming, in the Open question line or not at all. Don't add caveat paragraphs.
- Keep each cell to one line. The value is in the shape, not the prose.
- Stop after the plan. Execution starts when the user says go.