# gemini-docs

Small package for mirroring selected Gemini API docs into local markdown and
Python modules, plus an MCP server for agent lookup.

## Install and sync

```bash
pip install -e .
python main.py
```

This installs:
- `gemini-docs`: CLI to sync, list, and show docs
- `gemini-docs-mcp`: MCP server for coding agents

## CLI

```bash
gemini-docs sync
gemini-docs list
gemini-docs show text-generation
```

## Python API

```python
from gemini_docs import get_document, list_documents, search_documents

doc = get_document("text-generation")
print(doc.content)
print([item.slug for item in search_documents("function calling")])
```

## MCP

Run over stdio:

```bash
gemini-docs-mcp
```

Available tools:
- `list_documents`
- `get_document`
- `search_documents`
- `sync_documents`

Available resources:
- `gemini-docs://index`
- `gemini-docs://document/{slug}`

## CI

GitHub Actions runs:
- `ruff check .`
- `ruff format --check .`
- import smoke checks
- `python -m compileall gemini_docs main.py`
```
