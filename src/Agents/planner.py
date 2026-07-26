import json

from Graph.state import ResearchState
from llm import get_llm
from Prompts.planner_prompt import get_planner_prompt
from utils.llm_response import validate_llm_response


def planner_agent(state: ResearchState) -> ResearchState:
    """
    Generates a structured research plan from the user's query.
    """

    # Step 1: Validate input
    query = state["query"].strip()

    if not query:
        state["errors"].append(
            {
                "agent": "Planner Agent",
                "message": "Research query cannot be empty."
            }
        )
        return state

    try:
        # Step 2: Generate prompt
        prompt = get_planner_prompt(query)

        # Step 3: Get LLM instance
        llm = get_llm()

        # Step 4: Invoke LLM
        response = llm.invoke(prompt)

        # Step 5: Convert JSON string into Python object
        content = validate_llm_response(response)
        plan = json.loads(content)

        # Step 6: Assign IDs to each section
        for index, item in enumerate(plan, start=1):
            item["id"] = index

        # Step 7: Update state
        state["plan"] = plan

    except json.JSONDecodeError:
        state["errors"].append(
            {
                "agent": "Planner Agent",
                "message": "Invalid JSON received from LLM."
            }
        )

    except Exception as e:
        state["errors"].append(
            {
                "agent": "Planner Agent",
                "message": str(e)
            }
        )

    return state

