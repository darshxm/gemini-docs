from dataclasses import dataclass


@dataclass(frozen=True)
class GeminiDoc:
    slug: str
    title: str
    source_url: str
    module_name: str
    markdown_filename: str
    content: str


@dataclass(frozen=True)
class DocumentSpec:
    slug: str
    title: str
    url: str
    module_name: str
    markdown_filename: str
