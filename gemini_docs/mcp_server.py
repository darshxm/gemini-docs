from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from gemini_docs.generator import sync_docs
from gemini_docs.registry import get_document, list_documents, search_documents

server = FastMCP(
    name="gemini-docs",
    instructions=(
        "Lookup mirrored Gemini API documentation by slug or text search. "
        "Use the document resource when you need the full markdown content."
    ),
)


def _document_payload(doc) -> dict[str, str]:
    return {
        "slug": doc.slug,
        "title": doc.title,
        "source_url": doc.source_url,
        "module_name": doc.module_name,
        "markdown_filename": doc.markdown_filename,
        "content": doc.content,
    }


@server.tool(
    name="list_documents",
    description="List all available mirrored Gemini documentation topics.",
)
def list_documents_tool() -> list[dict[str, str]]:
    return [
        {
            "slug": doc.slug,
            "title": doc.title,
            "source_url": doc.source_url,
        }
        for doc in list_documents()
    ]


@server.tool(
    name="get_document",
    description="Get the full mirrored Gemini documentation content for a slug.",
)
def get_document_tool(slug: str) -> dict[str, str]:
    doc = get_document(slug)
    if doc is None:
        raise ValueError(f"Unknown slug: {slug}")
    return _document_payload(doc)


@server.tool(
    name="search_documents",
    description="Search mirrored Gemini documentation by substring match.",
)
def search_documents_tool(query: str, limit: int = 5) -> list[dict[str, str]]:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    matches = search_documents(query)[:limit]
    return [
        {
            "slug": doc.slug,
            "title": doc.title,
            "source_url": doc.source_url,
            "content_preview": doc.content[:500],
        }
        for doc in matches
    ]


@server.tool(
    name="sync_documents",
    description="Refresh mirrored docs from the configured Gemini documentation URLs.",
)
def sync_documents_tool(slugs: list[str] | None = None) -> list[dict[str, str]]:
    docs = sync_docs(slugs=slugs)
    return [
        {
            "slug": doc.slug,
            "title": doc.title,
            "source_url": doc.source_url,
        }
        for doc in docs
    ]


@server.resource(
    "gemini-docs://index",
    name="document-index",
    description="List of mirrored Gemini documentation topics.",
    mime_type="application/json",
)
def document_index_resource() -> list[dict[str, str]]:
    return list_documents_tool()


@server.resource(
    "gemini-docs://document/{slug}",
    name="document",
    description="Full mirrored Gemini documentation markdown for a single slug.",
    mime_type="text/markdown",
)
def document_resource(slug: str) -> str:
    doc = get_document(slug)
    if doc is None:
        raise ValueError(f"Unknown slug: {slug}")
    return doc.content


def serve(transport: str = "stdio") -> None:
    server.run(transport=transport)


def main() -> int:
    serve("stdio")
    return 0
