from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = (
    ROOT
    / "skills"
    / "figma-to-design-md"
    / "scripts"
    / "validate_output.py"
)
SPEC = importlib.util.spec_from_file_location("validate_output", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


DESIGN_TEMPLATE = """# Design System

## 1. Foundations

{tokens}

## 2. Layout

Layout rules.

## 3. Components

Component rules.

## 4. Page Patterns

Page rules.

## 5. Design Inconsistencies

None.

## 6. Figma References

Figma file and node references.
"""


def preview(properties: dict[str, str], required_css: str | None = None) -> str:
    declarations = "\n".join(
        f"      --{name}: {value};" for name, value in properties.items()
    )
    css = required_css or """
    @media (max-width: 768px) { main { padding: 1rem; } }
    button:focus-visible { outline: 2px solid var(--focus); }
    @media (prefers-reduced-motion: reduce) { * { transition: none; } }
    """
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Design preview</title>
  <style>
    :root {{
{declarations}
    }}
    {css}
  </style>
</head>
<body><main><section><button>Action</button></section></main></body>
</html>
"""


class ValidateOutputTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.light = {
            "surface": "#ffffff",
            "surface-muted": "#f5f5f5",
            "text": "#111111",
            "text-muted": "#666666",
            "border": "#dddddd",
            "action": "#0055cc",
            "danger": "#bb2222",
            "focus": "#2277ee",
        }
        self.dark = {
            "surface": "#111111",
            "surface-muted": "#1d1d1d",
            "text": "#f7f7f7",
            "text-muted": "#b5b5b5",
            "border": "#444444",
            "action": "#66a3ff",
            "danger": "#ff7777",
            "focus": "#88bbff",
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_suite(
        self,
        *,
        design_tokens: list[str] | None = None,
        light: dict[str, str] | None = None,
        dark: dict[str, str] | None = None,
        required_css: str | None = None,
    ) -> None:
        names = design_tokens if design_tokens is not None else list(self.light)
        token_text = "\n".join(f"- `--{name}`" for name in names)
        (self.root / "DESIGN.md").write_text(
            DESIGN_TEMPLATE.format(tokens=token_text), encoding="utf-8"
        )
        (self.root / "preview.html").write_text(
            preview(light or self.light, required_css), encoding="utf-8"
        )
        (self.root / "preview-dark.html").write_text(
            preview(dark or self.dark, required_css), encoding="utf-8"
        )

    def test_valid_suite_passes(self) -> None:
        self.write_suite()

        self.assertEqual([], VALIDATOR.validate_output(self.root))

    def test_css_requirements_in_comments_do_not_pass(self) -> None:
        fake_css = """
        /* @media (max-width: 768px) {}
           button:focus-visible {}
           @media (prefers-reduced-motion: reduce) {} */
        """
        self.write_suite(required_css=fake_css)

        errors = VALIDATOR.validate_output(self.root)

        self.assertTrue(any("responsive CSS" in error for error in errors))
        self.assertTrue(any(":focus-visible" in error for error in errors))
        self.assertTrue(any("reduced-motion" in error for error in errors))

    def test_themes_must_change_multiple_shared_tokens(self) -> None:
        weak_dark = dict(self.light)
        weak_dark["surface"] = "#000000"
        self.write_suite(dark=weak_dark)

        errors = VALIDATOR.validate_output(self.root)

        self.assertTrue(any("shared theme token values" in error for error in errors))

    def test_shared_preview_tokens_must_be_documented(self) -> None:
        self.write_suite(design_tokens=["surface"])

        errors = VALIDATOR.validate_output(self.root)

        self.assertTrue(any("missing from DESIGN.md" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
