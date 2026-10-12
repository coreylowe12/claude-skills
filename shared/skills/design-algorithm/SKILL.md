---
name: "design-algorithm"
description: "Runs Musk's 5-step design algorithm on an artifact, doc or design in progress, applies the changes, then reports them. Use on /design-algorithm or \"run the design algorithm\"."
---

# Design Algorithm

Put the current artifact, document or design through the five steps in order, make the changes in the work itself, then report back what changed.

## Output format

**Design:** [what is being designed and who it is for, in one sentence]

| # | Step | Change |
|---|------|--------|
| 1 | Make requirements less dumb | [which requirement was questioned or dropped, and why] |
| 2 | Delete | [what was removed] |
| 3 | Simplify | [what was made simpler among what survived] |
| 4 | Accelerate | [what now reads, loads or iterates faster] |
| 5 | Automate | [what is now templated, reusable or generated] |

**Added back:** [anything deleted then restored, or "Nothing"]

**Result:** [what is better now, in one sentence]

**Next:** [one concrete next step]

## How to do this well

- Run the steps in order; never simplify or speed up something that should have been deleted.
- Step 1: tie every requirement to the person it serves; question any requirement nobody owns.
- Step 2: delete sections, elements and words aggressively; if nothing ever needs adding back, you did not delete enough.
- Step 3: simplify only what survived step 2.
- Step 4: make it faster for the reader to scan and for us to revise.
- Step 5: automate last, and only what is stable.
- Apply the changes to the work itself before reporting; do not just suggest them.
- If a step changes nothing, write "No change" and the reason; never invent a change.
- One sentence per cell; honest over diplomatic.