from Graph.state import ResearchState

from llm import get_llm
from Prompts.summarizer_prompt import get_summary_prompt
from Utils.llm_response import validate_llm_response


def validate_summary_state(state: ResearchState) -> None:
    """
    Validate that the Summary Agent has the required state.

    Raises:
        ValueError: If the query or research data is invalid.
    """

    if not state["query"].strip():
        raise ValueError("Research query cannot be empty.")

    if not state["fact_checked_data"]:
        raise ValueError("No fact-checked data available to summarize.")


def build_research_document(research_data: dict[str, str]) -> str:
    """
    Convert the research dictionary into a structured Markdown document.
    """

    sections = []

    for section, content in research_data.items():
        sections.append(
            f"# {section}\n\n{content}"
        )

    return "\n\n".join(sections)


def save_summary(
    state: ResearchState,
    summary: str,
) -> None:
    """
    Save the generated summary into the shared state.
    """

    state["summary"] = summary


def summary_agent(state: ResearchState) -> ResearchState:
    """
    Consolidate all researched sections into a coherent summary.
    """

    try:
        # Step 1: Validate state
        validate_summary_state(state)

        # Step 2: Build research document
        research_document = build_research_document(
            state["fact_checked_data"]
        )

        # Step 3: Generate prompt
        prompt = get_summary_prompt(research_document)

        # Step 4: Invoke LLM
        llm = get_llm()
        response = llm.invoke(prompt)

        # Step 5: Validate response
        summary = validate_llm_response(response)

        # Step 6: Save summary
        save_summary(
            state=state,
            summary=summary,
        )

    except (ValueError, TypeError) as e:
        state["errors"].append(
            {
                "agent": "Summary Agent",
                "message": str(e),
            }
        )

    return state