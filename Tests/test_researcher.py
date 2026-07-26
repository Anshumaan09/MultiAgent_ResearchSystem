from Agents.Researcher import research_agent
from Graph.state import ResearchState


def main():

    state: ResearchState = {
        "query": "Agentic AI",
        "plan": [
            {
                "id": 1,
                "section": "Introduction",
                "objective": "Explain what Agentic AI is."
            }
        ],
        "current_plan_index": 0,
        "research_data": {},
        "summary_data": {},
        "fact_checked_data": {},
        "final_report": "",
        "errors": []
    }

    result = research_agent(state)

    print("\n===== RESEARCH DATA =====\n")
    print(result["research_data"])

    print("\n===== ERRORS =====\n")
    print(result["errors"])


if __name__ == "__main__":
    main()