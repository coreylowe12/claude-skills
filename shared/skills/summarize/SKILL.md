---
name: "summarize"
description: "Summarizes the entire conversation in a fixed format. Use when the user says /summarize or asks to summarize the whole thread."
---

# Summarize

Recap the whole thread so someone who wasn't in it can follow what happened and where it stands.

## Output format

Always use this exact structure:

**Goal:** [one sentence — what the thread set out to do]

**Outcome:** [one sentence — where things stand now]

| # | What we did | Result |
|---|---|---|
| 1 | [action, a few words] | [one sentence — specific names, numbers, links] |
| 2 | [action] | [result] |

**Decisions:**

| Decision | Why |
|---|---|
| [what was chosen] | [one sentence] |

**Open:** [one line per unfinished item or unverified claim, or "Nothing open."]

## How to do this well

- Cover the whole thread from the first message, not just the last few turns. Rows run in the order things happened.
- Be specific. Names, numbers, file names, and links beat descriptions.
- One sentence per cell. Merge small steps into one row; aim for 5 to 10 rows.
- If direction changed, say what was dropped and why in the Result cell.
- Be honest about what was tested and what wasn't. Anything unverified goes under Open.
- Leave out small talk and anything personal that isn't needed to understand the work.
- If there are no real decisions, drop the Decisions table instead of padding it.