from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from Graph.state import ResearchState

from Agents.supervisor import supervisor_agent
from Agents.planner import planner_agent
from Agents.Researcher import research_agent
from Agents.fact_checker import fact_checker_agent
from Agents.summarizer import summary_agent
from Agents.writer import writer_agent


def route_next_step(state: ResearchState) -> str:
    """
    Read the supervisor decision from the state.
    """

    return state["next_step"]


def build_graph() -> CompiledStateGraph:
    workflow: StateGraph = StateGraph(ResearchState)

    # Supervisor
    workflow.add_node("supervisor", supervisor_agent)

    # Worker agents
    workflow.add_node("planner", planner_agent)
    workflow.add_node("research", research_agent)
    workflow.add_node("fact_checker", fact_checker_agent)
    workflow.add_node("summary", summary_agent)
    workflow.add_node("writer", writer_agent)

    # Start with the supervisor
    workflow.add_edge(START, "supervisor")

    # Dynamic routing based on next_step
    workflow.add_conditional_edges(
        "supervisor",
        route_next_step,
        {
            "planner": "planner",
            "research": "research",
            "fact_checker": "fact_checker",
            "summary": "summary",
            "writer": "writer",
            "end": END,
        },
    )

    # After every worker, go back to the supervisor
    workflow.add_edge("planner", "supervisor")
    workflow.add_edge("research", "supervisor")
    workflow.add_edge("fact_checker", "supervisor")
    workflow.add_edge("summary", "supervisor")
    workflow.add_edge("writer", "supervisor")

    return workflow.compile()