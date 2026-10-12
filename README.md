# claude-skills

Generic Claude skills that work in any Claude account. One folder per skill, each with a `SKILL.md`.

**Keep personal skills out of this repo.** Anything with personal finances, journals, or home details lives in the separate `claude-skills-personal` folder, which is never cloned onto a work machine.

## What's here

| Skill | Use it for |
|---|---|
| `plan` | Goal first, then a short plan |
| `why` | 5 Whys root cause analysis ending in one fix |
| `handoff` | A copy-paste prompt that hands the work to a fresh session |
| `summarize` | Fixed-format recap of a whole thread |
| `assumptions` | What a statement, doc or plan takes for granted |
| `lint` | Fix anything stale against the latest decisions |
| `design-algorithm` | Musk's 5-step algorithm applied to a doc or design |
| `systems-engineer` | Map the parts of a setup and fix broken handoffs |

## Layout

```
.claude-plugin/marketplace.json   catalog, used only for the plugin route (option B)
shared/
  .claude-plugin/plugin.json      plugin manifest (bump "version" on each release)
  skills/<name>/SKILL.md          the skills
build_zips.py                     builds dist/<name>.zip, one per skill
```

## Get them into your work Claude

### A. Upload zips (default, no GitHub access needed on the work side)

1. `python3 build_zips.py` creates `dist/<name>.zip` for each skill and checks that each `name` matches its folder.
2. In work Claude: **Settings > Capabilities > Skills > Upload skill**, upload each zip, toggle it on.
3. If the Skills section is greyed out, **Code execution and file creation** or **Skills** is off for the org (on Enterprise an Owner turns these on in Admin settings > Capabilities), or **User-created skills** is disabled by policy. Ask an admin.

Uploaded skills are private to your account. Re-run the script and upload again after editing a skill; if Claude refuses a duplicate name, delete the old copy in Settings first.

### B. Plugin in Claude Code or Cowork (one-command updates)

On the work machine, in a Claude Code session:

```
/plugin marketplace add YOUR-GITHUB-USERNAME/claude-skills
/plugin install workflow-skills@corey-skills
```

This needs git access to the private repo from that machine. Check your employer's policy before putting personal GitHub credentials on a work computer. After editing a skill, bump `version` in `shared/.claude-plugin/plugin.json`, otherwise installs keep the cached copy.

### C. Org-wide (only if you want teammates to have them)

An Owner (or a member with a library-management role on Enterprise) can upload a plugin zip or sync a private GitHub repo in **Organization settings > Plugins & skills**. Sync needs the Claude GitHub App on the repo, and the repo must be private or internal. Not needed for personal use.

## Adding or changing a skill

- Start from `shared/skills/why/SKILL.md`: a title, one line of purpose, one fixed **Output format**, and a short **How to do this well** list.
- Folder name, `name:` in the frontmatter and the zip name must be identical (lowercase, hyphens).
- Say "the user", never a person's name, so the skill works for anyone.
- Run `python3 build_zips.py` to validate before uploading.
