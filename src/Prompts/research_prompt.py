from typing import Final


def get_research_prompt(section: str, objective: str) -> str:
    return f"""
Role:
You are an expert researcher.

Context:
You are responsible for researching one section of a larger report.

Section:
{section}

Objective:
{objective}

Task:
Generate detailed research for this section.

Constraints:
- Stay focused on this section only.
- Use factual information.
- Do not repeat information from other sections.
- Write in professional language.
- Use headings and bullet points where appropriate.

Output:
Return only the research text.
"""