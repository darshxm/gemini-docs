from __future__ import annotations

import importlib
from pathlib import Path

from gemini_docs.models import DocumentSpec, GeminiDoc
from gemini_docs.scraper import scrape_gemini_doc
from gemini_docs.sources import DOCUMENT_SPECS, DOCUMENT_SPECS_BY_SLUG

PACKAGE_ROOT = Path(__file__).resolve().parent
DOCS_DIR = PACKAGE_ROOT / "docs"
MARKDOWN_DIR = PACKAGE_ROOT / "markdown"


def _ensure_dirs() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    MARKDOWN_DIR.mkdir(exist_ok=True)


def _module_source(spec: DocumentSpec, content: str) -> str:
    return f'''"""Auto-generated from {spec.url}. Do not edit manually."""

from gemini_docs.models import GeminiDoc

SLUG = {spec.slug!r}
TITLE = {spec.title!r}
SOURCE_URL = {spec.url!r}
MODULE_NAME = {spec.module_name!r}
MARKDOWN_FILENAME = {spec.markdown_filename!r}
MARKDOWN = {content!r}

DOCUMENT = GeminiDoc(
    slug=SLUG,
    title=TITLE,
    source_url=SOURCE_URL,
    module_name=MODULE_NAME,
    markdown_filename=MARKDOWN_FILENAME,
    content=MARKDOWN,
)


def get_document() -> GeminiDoc:
    return DOCUMENT


def get_markdown() -> str:
    return MARKDOWN
'''


def _write_static_files() -> None:
    docs_init = DOCS_DIR / "__init__.py"
    if not docs_init.exists():
        docs_init.write_text("", encoding="utf-8")


def _write_doc_files(spec: DocumentSpec, content: str) -> GeminiDoc:
    markdown_path = MARKDOWN_DIR / spec.markdown_filename
    module_path = DOCS_DIR / f"{spec.module_name}.py"

    markdown_path.write_text(content, encoding="utf-8")
    module_path.write_text(_module_source(spec, content), encoding="utf-8")

    return GeminiDoc(
        slug=spec.slug,
        title=spec.title,
        source_url=spec.url,
        module_name=spec.module_name,
        markdown_filename=spec.markdown_filename,
        content=content,
    )


def _selected_specs(slugs: list[str] | None) -> list[DocumentSpec]:
    if not slugs:
        return list(DOCUMENT_SPECS)

    selected: list[DocumentSpec] = []
    for slug in slugs:
        try:
            selected.append(DOCUMENT_SPECS_BY_SLUG[slug])
        except KeyError as exc:
            raise ValueError(f"Unknown slug: {slug}") from exc
    return selected


def sync_docs(slugs: list[str] | None = None) -> list[GeminiDoc]:
    _ensure_dirs()
    _write_static_files()

    docs: list[GeminiDoc] = []
    for spec in _selected_specs(slugs):
        content = scrape_gemini_doc(spec.url)
        docs.append(_write_doc_files(spec, content))

    importlib.invalidate_caches()
    return docs
