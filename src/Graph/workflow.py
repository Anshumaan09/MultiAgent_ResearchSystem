from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from Graph.state import ResearchState
from Agents.planner import planner_agent
from Agents.Researcher import research_agent
from Agents.summarizer import summary_agent

def build_graph() -> CompiledStateGraph:
    workflow : StateGraph = StateGraph(ResearchState)

    workflow.add_node("planner", planner_agent)
    workflow.add_node("research", research_agent)
    workflow.add_node("summary", summary_agent)

    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "research")
    workflow.add_edge("research", "summary")
    workflow.add_edge("summary", END)

    return workflow.compile()