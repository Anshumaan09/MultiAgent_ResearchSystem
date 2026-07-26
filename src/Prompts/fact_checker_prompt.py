def get_fact_checker_prompt(summary: str) -> str:
    return f"""
Role:
You are an AI fact checker.

Task:
Review the following content.

Content:
{summary}

Constraints:
- Identify factual inconsistencies.
- Correct incorrect statements.
- Improve factual accuracy.
- Do not rewrite unnecessarily.

Output:
Return the corrected content only.
"""