import requests
from bs4 import BeautifulSoup, NavigableString


def get_md(node) -> str:
    if isinstance(node, NavigableString):
        return str(node)

    md = ""
    for child in node.children:
        if isinstance(child, NavigableString):
            md += str(child)
        elif child.name == "a":
            href = child.get("href", "")
            if href.startswith("/"):
                href = "https://ai.google.dev" + href
            md += f"[{get_md(child).strip()}]({href})"
        elif child.name == "code":
            md += f"`{get_md(child).strip()}`"
        elif child.name in ["strong", "b"]:
            md += f"**{get_md(child).strip()}**"
        else:
            md += get_md(child)
    return md


def scrape_gemini_doc(url: str, timeout: int = 30) -> str:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    body = soup.find("div", class_="devsite-article-body")
    if not body:
        raise ValueError(f"Could not find article body for {url}")

    lines: list[str] = []
    for elem in body.children:
        if isinstance(elem, NavigableString):
            continue

        if elem.name == "h2":
            lines.append(f"## {get_md(elem).strip()}")
            lines.append("")

        elif elem.name == "h3":
            lines.append(f"### {get_md(elem).strip()}")
            lines.append("")

        elif elem.name == "p":
            text = get_md(elem).strip()
            if text:
                lines.append(text)
                lines.append("")

        elif elem.name == "aside":
            text = " ".join(get_md(elem).strip().split())
            if text:
                lines.append(text)
                lines.append("")

        elif elem.name == "ul":
            for li in elem.find_all("li", recursive=False):
                text = " ".join(get_md(li).strip().split())
                lines.append(f"- {text}")
            lines.append("")

        elif elem.name == "div" and "ds-selector-tabs" in elem.get("class", []):
            python_section = None
            for section in elem.find_all("section"):
                h3 = section.find("h3")
                if h3 and "python" in h3.text.lower():
                    python_section = section
                    break

            if python_section:
                code_block = python_section.find("code")
                if code_block:
                    lines.append("### Python")
                    lines.append("")
                    lines.extend(f"    {line}" for line in code_block.text.split("\n"))
                    lines.append("")

    return "\n".join(lines).rstrip() + "\n"
