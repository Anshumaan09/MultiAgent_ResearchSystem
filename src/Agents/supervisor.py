from Graph.state import ResearchState


def supervisor_agent(state: ResearchState) -> ResearchState:
    """
    Determine which agent should execute next based on
    the current shared state.
    """

    try:
        # If there are workflow errors, stop execution
        if state["errors"]:
            state["next_step"] = "end"
            return state

        # Step 1: Need planning
        if not state["plan"]:
            state["next_step"] = "planner"

        # Step 2: Need research
        elif not state["research_data"]:
            state["next_step"] = "research"

        # Step 3: Need fact checking
        elif not state["fact_checked_data"]:
            state["next_step"] = "fact_checker"

        # Step 4: Need summary
        elif not state["summary"].strip():
            state["next_step"] = "summary"

        # Step 5: Need final report
        elif not state["final_report"].strip():
            state["next_step"] = "writer"

        # Everything is complete
        else:
            state["next_step"] = "end"

    except Exception as e:
        state["errors"].append(
            {
                "agent": "Supervisor Agent",
                "message": str(e),
            }
        )

        state["next_step"] = "end"

    return state