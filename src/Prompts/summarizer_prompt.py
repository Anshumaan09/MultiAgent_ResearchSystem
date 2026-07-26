def get_summary_prompt(research: str) -> str:
    return f"""
Role:
You are an expert technical research consolidator.

Task:
Consolidate the following research into a single coherent document.

Your objectives are:
- Remove duplicated information.
- Merge overlapping concepts.
- Preserve all important technical details.
- Maintain a logical flow between ideas.
- Improve readability without changing the meaning.

Research:
{research}

Constraints:
- Preserve factual accuracy.
- Do not introduce new information.
- Remove unnecessary repetition.
- Keep important technical terminology.
- Do not omit important concepts.

Output:
Return only the consolidated summary as plain text.
"""