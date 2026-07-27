from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from Graph.state import ResearchState
from Agents.planner import planner_agent
from Agents.Researcher import research_agent
from Agents.summarizer import summary_agent
from Agents.fact_checker import fact_checker_agent

def build_graph() -> CompiledStateGraph:
    workflow : StateGraph = StateGraph(ResearchState)

    workflow.add_node("planner", planner_agent)
    workflow.add_node("research", research_agent)
    workflow.add_node("fact_checker", fact_checker_agent)
    workflow.add_node("summary", summary_agent)


    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "research")
    workflow.add_edge("research", "fact_checker")
    workflow.add_edge("fact_checker", "summary")
    workflow.add_edge("summary", END)

    return workflow.compile()