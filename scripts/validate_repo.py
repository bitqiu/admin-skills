#!/usr/bin/env python3
"""Validate repository-level structure and deterministic skill metadata."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|lorem ipsum)\b", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ALLOWED_FRONTMATTER_KEYS = {
    "allowed-tools",
    "description",
    "license",
    "metadata",
    "name",
}


def frontmatter_value(header: str, key: str) -> str | None:
    lines = header.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:\s*(.*)$", line)
        if not match:
            continue
        value = match.group(1).strip()
        if value in {">", ">-", "|", "|-"}:
            parts: list[str] = []
            for continuation in lines[index + 1 :]:
                if continuation.startswith((" ", "\t")):
                    parts.append(continuation.strip())
                else:
                    break
            return " ".join(parts)
        return value.strip("\"'")
    return None


def quoted_yaml_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s+{re.escape(key)}:\s+([\"'])(.*?)\1\s*$", text)
    return match.group(2) if match else None


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        return [f"{skill_file}: invalid YAML frontmatter boundaries"]

    name = frontmatter_value(parts[1], "name")
    description = frontmatter_value(parts[1], "description")
    top_level_keys = {
        match.group(1)
        for line in parts[1].splitlines()
        if (match := re.match(r"^([a-zA-Z0-9_-]+):", line))
    }
    unexpected_keys = sorted(top_level_keys - ALLOWED_FRONTMATTER_KEYS)
    if unexpected_keys:
        errors.append(
            f"{skill_file}: unsupported frontmatter keys: {', '.join(unexpected_keys)}"
        )
    if name != skill_dir.name:
        errors.append(f"{skill_file}: name must match directory '{skill_dir.name}'")
    if not description:
        errors.append(f"{skill_file}: description is required")
    elif len(description) > 500:
        errors.append(f"{skill_file}: description should stay at or below 500 characters")
    if PLACEHOLDER.search(text):
        errors.append(f"{skill_file}: contains unfinished placeholder text")

    metadata_path = skill_dir / "agents" / "openai.yaml"
    if not metadata_path.is_file():
        errors.append(f"{metadata_path}: missing project-standard UI metadata")
    else:
        metadata = metadata_path.read_text(encoding="utf-8")
        display_name = quoted_yaml_value(metadata, "display_name")
        short_description = quoted_yaml_value(metadata, "short_description")
        default_prompt = quoted_yaml_value(metadata, "default_prompt")
        if not display_name:
            errors.append(f"{metadata_path}: display_name must be a quoted string")
        if not short_description or not 25 <= len(short_description) <= 64:
            errors.append(
                f"{metadata_path}: short_description must be a quoted 25-64 character string"
            )
        if not default_prompt or f"${skill_dir.name}" not in default_prompt:
            errors.append(
                f"{metadata_path}: default_prompt must be quoted and mention ${skill_dir.name}"
            )

    eval_path = skill_dir / "evals" / "evals.json"
    if not eval_path.is_file():
        errors.append(f"{eval_path}: missing eval definitions")
    else:
        try:
            data = json.loads(eval_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"{eval_path}: invalid JSON: {error}")
        else:
            if data.get("skill_name") != skill_dir.name:
                errors.append(f"{eval_path}: skill_name must match its directory")
            evals = data.get("evals")
            if not isinstance(evals, list) or not evals:
                errors.append(f"{eval_path}: evals must be a non-empty list")
            else:
                ids = [case.get("id") for case in evals]
                if len(ids) != len(set(ids)):
                    errors.append(f"{eval_path}: eval ids must be unique")
                for case in evals:
                    case_id = case.get("id", "unknown")
                    for field in ("prompt", "expected_output", "expectations", "files"):
                        if field not in case:
                            errors.append(f"{eval_path}: eval {case_id} is missing {field}")
                    if "expectations" in case and not case["expectations"]:
                        errors.append(f"{eval_path}: eval {case_id} has no expectations")
                    if "files" in case and not isinstance(case["files"], list):
                        errors.append(f"{eval_path}: eval {case_id} files must be a list")

    for markdown_path in skill_dir.rglob("*.md"):
        markdown = markdown_path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(markdown):
            clean_target = target.split("#", 1)[0]
            if not clean_target or "://" in clean_target or clean_target.startswith("mailto:"):
                continue
            if not (markdown_path.parent / clean_target).resolve().exists():
                errors.append(f"{markdown_path}: broken relative link '{target}'")

    for script_path in skill_dir.rglob("*.py"):
        try:
            ast.parse(script_path.read_text(encoding="utf-8"), filename=str(script_path))
        except SyntaxError as error:
            errors.append(f"{script_path}: Python syntax error: {error}")
    return errors


def main() -> int:
    errors: list[str] = []
    if not SKILLS_ROOT.is_dir():
        errors.append(f"Missing skills source directory: {SKILLS_ROOT}")
    else:
        skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
        if not skill_dirs:
            errors.append(f"No skills found in {SKILLS_ROOT}")
        for skill_dir in skill_dirs:
            errors.extend(validate_skill(skill_dir))

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    count = len([path for path in SKILLS_ROOT.iterdir() if path.is_dir()])
    print(f"Repository validation passed: {count} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
