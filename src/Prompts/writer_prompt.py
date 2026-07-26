def get_writer_prompt(research_sections: str) -> str:
    return f"""
Role:
You are a professional technical writer.

Task:
Convert the following researched sections into a polished report.

Content:
{research_sections}

Constraints:
- Use Markdown.
- Maintain logical flow.
- Use headings and subheadings.
- Preserve all important information.
- Write professionally.

Output:
Return the final report in Markdown.
"""