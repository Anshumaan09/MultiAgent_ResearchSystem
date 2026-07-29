def get_research_prompt(
    topic: str,
    section: str,
    objective: str,
    web_context: str,
) -> str:
    return f"""
Role:
You are an expert researcher.

Task:
Write a detailed research section using the provided web search results.

Research Topic:
{topic}

Section:
{section}

Objective:
{objective}

Web Search Results:
{web_context}

Instructions:
- Use ONLY the information provided in the web search results.
- Synthesize the information into a coherent research section.
- Do not invent facts or citations.
- If the provided information is limited, clearly mention that the available sources provide limited details.
- Write in a professional, factual, and well-structured style.
- Focus specifically on the given section and objective.

Output:
Return only the research content for this section.
"""
