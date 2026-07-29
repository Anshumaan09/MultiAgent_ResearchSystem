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
print("\n===== FINAL REPORT =====\n") 
print(result["final_report"]) 
print("\n===== ERRORS =====\n") 
print(result["errors"]) 
with open("workflow_output.md", "w", encoding="utf-8") as file: 
    file.write(result["final_report"])