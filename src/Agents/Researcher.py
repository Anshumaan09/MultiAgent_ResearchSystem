from Graph.state import ResearchState, PlanItem

from Prompts.research_prompt import get_research_prompt

from llm import get_llm

from Utils.llm_response import validate_llm_response
from Utils.web_search import search_web


def validate_research_state(state: ResearchState) -> None:
    """
    Validate that the research agent has the required state.

    Raises:
        ValueError: If the state is invalid.
    """

    if not state["query"].strip():
        raise ValueError("Research query cannot be empty.")

    if not state["plan"]:
        raise ValueError("Research plan is empty.")

    index = state["current_plan_index"]

    if not (0 <= index < len(state["plan"])):
        raise IndexError(
            f"Invalid current_plan_index: {index}. "
            f"Expected a value between 0 and {len(state['plan']) - 1}."
        )


def get_current_plan_item(state: ResearchState) -> PlanItem:
    """
    Return the current plan item based on the execution index.
    """

    index = state["current_plan_index"]
    return state["plan"][index]


def save_research(
    state: ResearchState,
    section_name: str,
    research_text: str,
) -> None:
    """
    Save the research output for a section.
    """

    state["research_data"][section_name] = research_text


def research_agent(state: ResearchState) -> ResearchState:
    """
    Research the current section defined by the planner and
    store the result in the shared state.
    """

    try:
        # Step 1: Validate state
        validate_research_state(state)

        # Step 2: Get current section
        plan_item = get_current_plan_item(state)

        topic = state["query"]
        section = plan_item["section"]
        objective = plan_item["objective"]

        # Step 3: Search the web for relevant information
        web_context = search_web(
            query=f"{topic} - {objective}"
        )

        # Step 4: Build prompt using web search results
        prompt = get_research_prompt(
            topic=topic,
            section=section,
            objective=objective,
            web_context=web_context,
        )

        # Step 5: Invoke LLM
        llm = get_llm()
        response = llm.invoke(prompt)

        # Step 6: Validate response
        content = validate_llm_response(response)

        # Step 7: Save research
        save_research(
            state=state,
            section_name=section,
            research_text=content,
        )

    except (ValueError, TypeError, IndexError) as e:
        state["errors"].append(
            {
                "agent": "Research Agent",
                "message": str(e),
            }
        )

    return state
