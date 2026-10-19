#!/usr/bin/env python3
"""Verify the pinned package and both clients' local marketplace contracts."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
lock = json.loads((ROOT / "docs/source-lock.json").read_text())
plugin = ROOT / "plugins/skill-studio"
files = {str(p.relative_to(plugin)): hashlib.sha256(p.read_bytes()).hexdigest()
         for p in sorted(plugin.rglob("*")) if p.is_file()}
assert files == lock["files"], "Package differs from source lock"
digest = hashlib.sha256("".join(f"{v}  {k}\n" for k, v in files.items()).encode()).hexdigest()
assert digest == lock["package_sha256"], "Aggregate hash differs"
for client in [".claude-plugin", ".codex-plugin"]:
    manifest = json.loads((plugin / client / "plugin.json").read_text())
    assert manifest["name"] == "skill-studio" and manifest["version"] == lock["version"]
for path in [".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"]:
    catalog = json.loads((ROOT / path).read_text())
    assert catalog["name"] == "dcbkk-plugins" and len(catalog["plugins"]) == 1
    entry = catalog["plugins"][0]
    assert entry["name"] == "skill-studio"
    source = entry["source"]
    assert (source if isinstance(source, str) else source["path"]) == "./plugins/skill-studio"
    if isinstance(source, dict):
        assert source["source"] == "local"
        assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
# Keep upstream hashes and prove the exact, bounded event patch.
for relative, original_hash in lock["upstream_files"].items():
    content = (plugin / relative).read_bytes()
    if relative in {"skills/create-skill/SKILL.md", "skills/improve-skill/SKILL.md", "skills/tidy-skill/SKILL.md"}:
        assert content.count(b"user-invocable: false\n") == 1
        content = content.replace(b"user-invocable: false\n", b"", 1)
    elif relative in {".claude-plugin/plugin.json", ".codex-plugin/plugin.json"}:
        original = json.loads(content)
        original["version"] = lock["upstream_version"]
        if relative.startswith(".codex-plugin/"):
            assert original["skills"] == "./skills/skill-studio"
            original["skills"] = "./skills"
        content = (json.dumps(original, indent=2) + "\n").encode()
    assert hashlib.sha256(content).hexdigest() == original_hash, f"Unexpected upstream change: {relative}"
assert "user-invocable: false" not in (plugin / "skills/skill-studio/SKILL.md").read_text()
expected = {"skill-studio", "create-skill", "improve-skill", "tidy-skill"}
assert {p.parent.name for p in plugin.glob("skills/*/SKILL.md")} == expected
for path in plugin.rglob("*.md"):
    for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text()):
        if "://" not in target and not target.startswith("#"):
            assert (path.parent / target).exists(), f"Broken link: {path.relative_to(plugin)} -> {target}"
assert not any(p.is_symlink() for p in plugin.rglob("*")), "Unexpected package symlink"
print(f"PASS: both catalogs, 4 skills, relative links, {len(files)} exact files; sha256 {digest}")
