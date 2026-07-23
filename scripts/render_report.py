#!/usr/bin/env python3
"""Render a Markdown SaaS audit report to HTML and optionally PDF."""

from __future__ import annotations

import argparse
import html
import shutil
import subprocess
import sys
from pathlib import Path


def markdown_to_html(markdown_text: str, title: str) -> str:
    try:
        import markdown  # type: ignore

        body = markdown.markdown(
            markdown_text,
            extensions=["tables", "fenced_code", "toc", "sane_lists"],
        )
    except ImportError:
        body = f"<pre>{html.escape(markdown_text)}</pre>"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root {{ color-scheme: light dark; }}
body {{ max-width: 1100px; margin: 0 auto; padding: 40px; font: 16px/1.55 system-ui, sans-serif; }}
h1, h2, h3 {{ line-height: 1.2; }}
table {{ border-collapse: collapse; width: 100%; margin: 1rem 0; }}
th, td {{ border: 1px solid #8886; padding: .55rem; text-align: left; vertical-align: top; }}
code, pre {{ font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }}
pre {{ overflow: auto; padding: 1rem; border: 1px solid #8886; border-radius: 8px; }}
blockquote {{ border-left: 4px solid #8888; margin-left: 0; padding-left: 1rem; }}
@media print {{ body {{ max-width: none; padding: 12mm; }} a {{ color: inherit; text-decoration: none; }} }}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def render_pdf(html_path: Path, pdf_path: Path) -> bool:
    candidates = [
        ["wkhtmltopdf", str(html_path), str(pdf_path)],
        ["weasyprint", str(html_path), str(pdf_path)],
    ]
    chromium = next(
        (shutil.which(name) for name in ["chromium", "chromium-browser", "google-chrome", "chrome"] if shutil.which(name)),
        None,
    )
    if chromium:
        candidates.append(
            [
                chromium,
                "--headless",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                f"--print-to-pdf={pdf_path}",
                html_path.resolve().as_uri(),
            ]
        )

    for command in candidates:
        if shutil.which(command[0]) is None:
            continue
        try:
            subprocess.run(command, check=True, timeout=120, capture_output=True, text=True)
            if pdf_path.exists() and pdf_path.stat().st_size > 0:
                return True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
            continue
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Markdown report")
    parser.add_argument("--html", type=Path, help="HTML output path")
    parser.add_argument("--pdf", type=Path, help="Optional PDF output path")
    parser.add_argument("--title", default="SaaS Audit Report")
    args = parser.parse_args()

    try:
        markdown_text = args.input.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Unable to read {args.input}: {exc}", file=sys.stderr)
        return 2

    html_path = args.html or args.input.with_suffix(".html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(markdown_to_html(markdown_text, args.title), encoding="utf-8")
    print(f"HTML: {html_path}")

    if args.pdf:
        args.pdf.parent.mkdir(parents=True, exist_ok=True)
        if render_pdf(html_path, args.pdf):
            print(f"PDF: {args.pdf}")
        else:
            print("PDF renderer unavailable; HTML was created successfully.", file=sys.stderr)
            return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
