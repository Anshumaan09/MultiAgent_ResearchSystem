from Graph.state import ResearchState
from llm import get_llm
from Prompts.writer_prompt import get_writer_prompt
from Utils.llm_response import validate_llm_response
from Utils.document_builder import build_markdown_document


def validate_writer_state(state: ResearchState) -> None:
    """
    Validate that the Writer Agent has the required state.

    Raises:
        ValueError: If the required data is missing.
    """

    if not state["query"].strip():
        raise ValueError("Research query cannot be empty.")

    if not state["summary"].strip():
        raise ValueError("Summary cannot be empty.")

    if not state["fact_checked_data"]:
        raise ValueError("No fact-checked data available to write the report.")


def build_research_document(
    fact_checked_data: dict[str, str]
) -> str:
    """
    Convert the fact-checked research dictionary into
    a structured Markdown document.
    """

    sections = []

    for section, content in fact_checked_data.items():
        sections.append(
            f"# {section}\n\n{content}"
        )

    return "\n\n".join(sections)


def save_report(
    state: ResearchState,
    report: str,
) -> None:
    """
    Save the generated report into the shared state.
    """

    state["final_report"] = report


def writer_agent(state: ResearchState) -> ResearchState:
    """
    Convert the verified research into a professional report.
    """

    try:
        # Step 1: Validate state
        validate_writer_state(state)

        # Step 2: Build document
        research_document = build_markdown_document(
            state["fact_checked_data"]
        )

        # Step 3: Build prompt
        prompt = get_writer_prompt(
            query=state["query"],
            summary=state["summary"],
            research_document=research_document,
        )

        # Step 4: Invoke LLM
        llm = get_llm()
        response = llm.invoke(prompt)

        # Step 5: Validate response
        report = validate_llm_response(response)

        # Step 6: Save report
        save_report(
            state=state,
            report=report,
        )

    except (ValueError, TypeError) as e:
        state["errors"].append(
            {
                "agent": "Writer Agent",
                "message": str(e),
            }
        )

    return state