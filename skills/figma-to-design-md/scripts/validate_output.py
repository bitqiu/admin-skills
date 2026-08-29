#!/usr/bin/env python3
"""Validate deterministic parts of a figma-to-design-md output suite."""

from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


REQUIRED_FILES = ("DESIGN.md", "preview.html", "preview-dark.html")
REQUIRED_DESIGN_SECTIONS = (
    "Foundations",
    "Layout",
    "Components",
    "Page Patterns",
    "Design Inconsistencies",
    "Figma References",
)
PLACEHOLDERS = re.compile(
    r"\b(?:TODO|TBD|lorem ipsum)\b|\[insert\b|\[figma file\]|\[pages, modes",
    re.IGNORECASE,
)
CUSTOM_PROPERTY = re.compile(r"--([a-zA-Z0-9_-]+)\s*:")


class PreviewParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: set[str] = set()
        self.has_lang = False
        self.has_title = False
        self.has_viewport = False

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.tags.add(tag)
        values = dict(attrs)
        if tag == "html" and values.get("lang"):
            self.has_lang = True
        if tag == "title":
            self.has_title = True
        if tag == "meta" and values.get("name", "").lower() == "viewport":
            self.has_viewport = True


def validate_design(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not re.search(r"(?m)^# Design System\s*$", text):
        errors.append("DESIGN.md must include the '# Design System' title")
    for section in REQUIRED_DESIGN_SECTIONS:
        pattern = rf"(?m)^## (?:\d+\.\s*)?{re.escape(section)}\s*$"
        if not re.search(pattern, text):
            errors.append(f"DESIGN.md is missing the '{section}' section")
    if PLACEHOLDERS.search(text):
        errors.append("DESIGN.md contains placeholder text")
    return errors


def validate_preview(path: Path) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    parser = PreviewParser()
    parser.feed(text)

    if not re.match(r"\s*<!doctype html>", text, re.IGNORECASE):
        errors.append(f"{path.name} is missing an HTML5 doctype")
    if not parser.has_lang:
        errors.append(f"{path.name} must set the html lang attribute")
    if not parser.has_viewport:
        errors.append(f"{path.name} is missing a viewport meta tag")
    if not parser.has_title:
        errors.append(f"{path.name} is missing a title")
    for tag in ("style", "main", "section"):
        if tag not in parser.tags:
            errors.append(f"{path.name} must contain a <{tag}> element")
    if "@media" not in text:
        errors.append(f"{path.name} must include responsive CSS")
    if ":focus-visible" not in text:
        errors.append(f"{path.name} must define a visible :focus-visible state")
    if "prefers-reduced-motion" not in text:
        errors.append(f"{path.name} must handle reduced-motion preferences")
    if PLACEHOLDERS.search(text):
        errors.append(f"{path.name} contains placeholder text")

    properties = set(CUSTOM_PROPERTY.findall(text))
    if len(properties) < 8:
        errors.append(f"{path.name} must expose at least eight CSS custom properties")
    return errors, properties


def validate_output(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.is_dir():
        return [f"Output directory does not exist: {root}"]

    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"Missing required file: {name}")
    if errors:
        return errors

    errors.extend(validate_design(root / "DESIGN.md"))
    light_errors, light_properties = validate_preview(root / "preview.html")
    dark_errors, dark_properties = validate_preview(root / "preview-dark.html")
    errors.extend(light_errors)
    errors.extend(dark_errors)

    if (root / "preview.html").read_bytes() == (root / "preview-dark.html").read_bytes():
        errors.append("Light and dark previews must not be identical")
    shared_properties = light_properties & dark_properties
    if len(shared_properties) < 8:
        errors.append(
            "Light and dark previews must share at least eight semantic CSS token names"
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    args = parser.parse_args()
    root = args.project_root.expanduser().resolve()

    errors = validate_output(root)
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
