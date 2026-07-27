from Graph.state import ResearchState
from llm import get_llm
from Prompts.fact_checker_prompt import get_fact_checker_prompt
from Utils.llm_response import validate_llm_response


def fact_checker_agent(state: ResearchState) -> ResearchState:
    """
    Reviews each research section for factual accuracy.
    """

    verified_data = {}
    errors = state["errors"]

    for section, content in state["research_data"].items():
        try:
            prompt = get_fact_checker_prompt(
                section=section,
                content=content
            )
            llm = get_llm()
            response = llm.invoke(prompt)
            verified_content = validate_llm_response(response)
            verified_data[section] = verified_content

        except Exception as e:
            errors.append({
                "agent": "Fact Checker",
                "message": f"Failed to verify section '{section}': {str(e)}"
            })

    state["fact_checked_data"] = verified_data

    return state