def get_summary_prompt(research: str) -> str:
    return f"""
Role:
You are an expert summarizer.

Task:
Summarize the following research while preserving all important information.

Research:
{research}

Constraints:
- Keep factual accuracy.
- Remove unnecessary repetition.
- Keep technical terms.

Output:
Return only the summary.
"""