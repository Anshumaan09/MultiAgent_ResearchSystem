from typing import Final


def get_planner_prompt(query: str) -> str:
    return f"""
Role:
You are an expert research planner.

Context:
You are the first agent in a multi-agent research system. Your task is to create a structured research plan that will be executed by specialized AI agents.

Task:
Break the research topic into exactly 5 logical and independent sections.

Research Topic:
{query}

Constraints:
- Create exactly 5 sections.
- Sections must not overlap.
- Each section must have a clear objective.
- Objectives should be concise.
- Arrange sections in a logical learning order.

Output Format:
Return ONLY valid JSON.

Example:
[
    {{
        "section": "Introduction",
        "objective": "Explain the basic concept."
    }}
]
"""