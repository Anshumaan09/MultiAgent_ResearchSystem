def get_fact_checker_prompt(section: str, content: str) -> str:
    return f"""
Role:
You are an expert fact-checker and technical reviewer.

Task:
Review the following research section for factual accuracy.

Section:
{section}

Content:
{content}

Instructions:
- Correct factual inaccuracies.
- Remove unsupported or misleading claims.
- Preserve all correct information.
- Do not invent new facts or add information that is not supported.
- Maintain the original meaning and level of detail.
- Keep the writing clear, professional, and well-structured.

Output:
Return only the corrected content.
"""