#!/usr/bin/env python3
"""Build one upload-ready zip per skill.

Usage:
    python3 build_zips.py [skills_dir] [out_dir]

Defaults: skills_dir = shared/skills (or skills/ if that doesn't exist), out_dir = dist.
Each zip has the skill folder at its root (<name>/SKILL.md, ...), which is the
shape Settings > Capabilities > Skills > Upload skill expects.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FIXED_TIME = (2020, 1, 1, 0, 0, 0)  # deterministic zips: unchanged skills rebuild identically
SKIP = {".DS_Store", "Thumbs.db"}


def read_frontmatter(skill_md: Path) -> dict:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        raise ValueError("no frontmatter block")
    out = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^(name|description):\s*(.+?)\s*$", line)
        if not kv:
            continue
        key, val = kv.groups()
        out[key] = json.loads(val) if val.startswith('"') else val.strip("'")
    return out


def main() -> int:
    here = Path(__file__).resolve().parent
    default_src = here / "shared" / "skills"
    if not default_src.exists():
        default_src = here / "skills"
    src = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else default_src
    out = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else here / "dist"

    if not src.is_dir():
        print(f"Skills folder not found: {src}")
        return 1
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("*.zip"):
        old.unlink()

    errors, built = [], []
    for folder in sorted(p for p in src.iterdir() if p.is_dir() and not p.name.startswith(".")):
        skill_md = folder / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{folder.name}: missing SKILL.md")
            continue
        try:
            fm = read_frontmatter(skill_md)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{folder.name}: bad frontmatter ({e})")
            continue
        name, desc = fm.get("name"), fm.get("description")
        if not name or not desc:
            errors.append(f"{folder.name}: frontmatter needs both name and description")
        elif name != folder.name:
            errors.append(f"{folder.name}: name '{name}' must match the folder name")
        elif not NAME_RE.match(name):
            errors.append(f"{folder.name}: name must be lowercase letters, numbers and hyphens")
        elif len(desc) > 1024:
            errors.append(f"{folder.name}: description is {len(desc)} chars (max 1024)")
        else:
            zpath = out / f"{name}.zip"
            with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as zf:
                for f in sorted(folder.rglob("*")):
                    if f.is_file() and f.name not in SKIP:
                        info = zipfile.ZipInfo(f"{name}/{f.relative_to(folder).as_posix()}", FIXED_TIME)
                        info.compress_type = zipfile.ZIP_DEFLATED
                        info.external_attr = 0o644 << 16
                        zf.writestr(info, f.read_bytes())
            built.append(zpath.name)

    for b in built:
        print(f"built  {out.name}/{b}")
    for e in errors:
        print(f"ERROR  {e}")
    print(f"\n{len(built)} zip(s) built, {len(errors)} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
