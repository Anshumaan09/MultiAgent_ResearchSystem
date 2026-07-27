from Graph.workflow import build_graph

workflow = build_graph()

initial_state = {
    "query": "What is Agentic AI?",
    "plan": [],
    "current_plan_index": 0,
    "research_data": {},
    "summary": "",
    "fact_checked_data": {},
    "final_report": "",
    "errors": []
}

result = workflow.invoke(initial_state)

print(result["summary"])
print(result["errors"])