def build_markdown_document(
    sections: dict[str, str]
) -> str:
    """
    Convert a dictionary of section names and contents
    into a Markdown document.

    Example
    -------
    Input:
    {
        "Introduction": "...",
        "Applications": "..."
    }

    Output:

    # Introduction

    ...

    # Applications

    ...
    """

    markdown_sections = []

    for heading, content in sections.items():
        markdown_sections.append(
            f"# {heading}\n\n{content}"
        )

    return "\n\n".join(markdown_sections)