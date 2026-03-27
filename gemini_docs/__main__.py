import argparse
import sys

from gemini_docs.generator import sync_docs
from gemini_docs.mcp_server import serve
from gemini_docs.registry import get_document, list_documents


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gemini-docs")
    subparsers = parser.add_subparsers(dest="command")

    sync_parser = subparsers.add_parser("sync")
    sync_parser.add_argument(
        "--slug",
        action="append",
        dest="slugs",
        help="Sync only the selected slug. Repeat to include multiple docs.",
    )

    subparsers.add_parser("list")

    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("slug")

    mcp_parser = subparsers.add_parser("mcp")
    mcp_parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    command = args.command or "sync"

    if command == "sync":
        docs = sync_docs(slugs=getattr(args, "slugs", None))
        for doc in docs:
            print(f"{doc.slug}: {doc.source_url}")
        return 0

    if command == "list":
        for doc in list_documents():
            print(f"{doc.slug}: {doc.title}")
        return 0

    if command == "show":
        doc = get_document(args.slug)
        if doc is None:
            print(f"Unknown slug: {args.slug}", file=sys.stderr)
            return 1
        print(doc.content, end="")
        return 0

    if command == "mcp":
        serve(transport=args.transport)
        return 0

    parser.print_help()
    return 1
