from __future__ import annotations

import importlib
import pkgutil

from gemini_docs.models import GeminiDoc

DOCS_PACKAGE = "gemini_docs.docs"


def _iter_doc_modules():
    package = importlib.import_module(DOCS_PACKAGE)
    for module_info in pkgutil.iter_modules(package.__path__):
        if module_info.name.startswith("_"):
            continue
        yield importlib.import_module(f"{DOCS_PACKAGE}.{module_info.name}")


def list_documents() -> list[GeminiDoc]:
    docs = [module.DOCUMENT for module in _iter_doc_modules()]
    return sorted(docs, key=lambda item: item.slug)


def get_document(slug: str) -> GeminiDoc | None:
    for doc in list_documents():
        if doc.slug == slug:
            return doc
    return None


def search_documents(query: str) -> list[GeminiDoc]:
    needle = query.lower()
    return [
        doc
        for doc in list_documents()
        if needle in doc.slug.lower()
        or needle in doc.title.lower()
        or needle in doc.content.lower()
    ]
