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
    assert catalog["name"] == "dcbkk-plugins"
    assert {entry["name"] for entry in catalog["plugins"]} == {"skill-studio", "humanizer"}
    assert len(catalog["plugins"]) == 2
    for entry in catalog["plugins"]:
        source = entry["source"]
        assert (source if isinstance(source, str) else source["path"]) == "./plugins/" + entry["name"]
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
humanizer = ROOT / "plugins/humanizer"
humanizer_lock = json.loads((ROOT / "docs/humanizer-source-lock.json").read_text())
humanizer_files = {str(p.relative_to(humanizer)): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in sorted(humanizer.rglob("*")) if p.is_file()}
assert humanizer_files == humanizer_lock["files"], "Humanizer differs from exact published package"
humanizer_digest = hashlib.sha256("".join(f"{v}  {k}\n" for k, v in humanizer_files.items()).encode()).hexdigest()
assert humanizer_digest == humanizer_lock["package_sha256"]
for relative, original_hash in humanizer_lock["upstream_files"].items():
    event_relative = relative.replace("skills/content-humanizer/", "skills/humanizer/")
    content = (humanizer / event_relative).read_bytes()
    if relative in {".claude-plugin/plugin.json", ".codex-plugin/plugin.json"}:
        original = json.loads(content)
        original["name"] = "content-humanizer"
        original["displayName"] = "Content Humanizer"
        original["version"] = humanizer_lock["upstream_version"]
        if "interface" in original:
            original["interface"]["displayName"] = "Content Humanizer"
        content = (json.dumps(original, indent=2) + "\n").encode()
    elif relative.endswith((".md", ".py")):
        content = content.replace(b"skills/humanizer", b"skills/content-humanizer")
        content = content.replace(b"name: humanizer\n", b"name: content-humanizer\n")
        if Path(relative).name in {"README.md", "SKILL.md", "AGENTS.md"}:
            content = content.replace(b"# Humanizer", b"# Content Humanizer")
    assert hashlib.sha256(content).hexdigest() == original_hash, f"Unexpected Humanizer content change: {relative}"

for client in [".claude-plugin", ".codex-plugin"]:
    manifest = json.loads((humanizer / client / "plugin.json").read_text())
    assert manifest["name"] == "humanizer" and manifest["version"] == humanizer_lock["version"]
assert [p.parent.name for p in humanizer.glob("skills/*/SKILL.md")] == ["humanizer"]
assert "user-invocable: false" not in (humanizer / "skills/humanizer/SKILL.md").read_text().split("---", 2)[1]
for plugin_root in [plugin, humanizer]:
    for path in plugin_root.rglob("*.md"):
        for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", path.read_text()):
            if "://" not in target and not target.startswith("#"):
                assert (path.parent / target).exists(), f"Broken link: {path.relative_to(plugin_root)} -> {target}"
    assert not any(p.is_symlink() for p in plugin_root.rglob("*")), "Unexpected package symlink"
print(f"PASS: both catalogs contain only 2 plugins; Skill Studio {len(files)} files and Humanizer {len(humanizer_files)} files match their locks; relative links resolve")
