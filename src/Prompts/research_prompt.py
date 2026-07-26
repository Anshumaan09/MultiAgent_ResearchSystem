from typing import Final


def get_research_prompt(topic: str, section: str, objective: str) -> str:
    return f"""
Role:
You are an expert researcher.

Context:
You are responsible for researching one section of a larger report.
The overall topic of the report is: {topic}

Section:
{section}

Objective:
{objective}

Task:
Generate detailed research for this section.

Instructions:
- Research only this section.
- Stay focused on the objective.
- Write 500-700 words.
- Use clear technical language.
- Do not include Markdown headings.
- Return plain text only.

Constraints:
- Stay focused on this section only.
- Use factual information.
- Do not repeat information from other sections.
- Write in professional language.
- Use headings and bullet points where appropriate.

Output:
Return only the research text.
"""