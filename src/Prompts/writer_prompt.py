def get_writer_prompt(
    query: str,
    summary: str,
    research_document: str,
) -> str:
    return f"""
Role:
You are a senior technical report writer.

Task:
Write a polished, professional technical research report using the verified research provided.

Research Topic:
{query}

Executive Summary:
{summary}

Verified Research:
{research_document}

Instructions:

- Generate a professional report title.
- Use Markdown formatting.
- Organize the report using clear headings.
- Start with an Executive Summary.
- Present each research section logically.
- Improve readability and flow.
- Preserve all factual accuracy.
- Do not introduce new facts.
- Do not remove important technical information.
- End with a concise conclusion.

Output:

Return only the completed Markdown report.
"""