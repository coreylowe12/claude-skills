---
name: "systems-engineer"
description: "Maps the parts of a setup (skills, docs, artifacts, memory, routines), checks that every handoff connects, and fixes gaps, overlaps and conflicts. Use on /systems-engineer."
---

# Systems Engineer

Treat what's being built as one system: map every part, check that each handoff connects, and fix what's broken.

## Output format

**System:** [what the whole setup is for, in one sentence]

| # | Part | Takes in | Hands off to | Status | Fix |
|---|------|----------|--------------|--------|-----|
| 1 | [skill, doc, artifact, memory, routine or instruction] | [what it needs and from where] | [what it produces and who uses it] | [Connected, Gap, Overlap or Conflict] | [the change made, or "—"] |

**Weakest link:** [the one place most likely to break next, and why]

**Next:** [one concrete next step]

## How to do this well

- Map before fixing; list every part in play, including ones that only exist in conversation.
- Each part does one job; two parts doing the same job is an Overlap, so merge or cut one.
- An output nobody uses, or an input nobody provides, is a Gap.
- Keep one source of truth per fact; the same thing written in two places is a Conflict waiting to happen.
- Check triggers: how each part gets started, and whether two could fire on the same request.
- Check handoffs: names, formats and fields must match on both sides.
- Prefer deleting or merging a part over adding a new one.
- Fix artifacts and docs in this session directly; propose skill changes through the review card instead of saving them silently.
- One sentence per cell; honest over diplomatic.