---
name: "handoff"
description: "Writes a one-click-copy session prompt to hand the work to another session or tool. Use when the user says /handoff or wants to pass the thread on."
---

# Handoff

Package the thread so a fresh session can pick it up cold. The prompt is the deliverable.

## Output format

Always use this exact structure:

**Goal:** [one sentence — what the next session should accomplish]

**State:** [one sentence — what exists now and where it lives]

**Session prompt** (use the copy button, then paste):

```text
[the prompt]
```

The prompt always has these parts, in this order, as plain text with short labeled sections (no tables, no markdown headers):

Goal: [what to accomplish]
Context: [what this is and where it lives: links, file paths, names]
Done so far: [the key steps and results]
Decisions to keep: [choices already made, with the reason when it isn't obvious]
Constraints: [what must not break: technical limits, data shape, names the code depends on]
Not verified: [what was never tested or checked]
First step: [the one thing to do first]

## How to do this well

- The prompt must stand alone. The next session has none of this thread, so never write "as discussed" or "above".
- Put everything in a single fenced code block so the copy button copies all of it. Don't put triple backticks inside it; indent code or paths instead.
- Use exact links, file paths, ids, and names. If a file or page is the deliverable, say how to open it.
- Aim the prompt at the destination. If the user named a tool or role (design pass, code review), shape the Goal and First step for it.
- One goal per handoff. Keep the prompt under about 500 words unless the work truly needs more.
- Be honest about unfinished and unverified parts. Don't present guesses as facts.
- Leave out personal details and chatter the next session doesn't need.