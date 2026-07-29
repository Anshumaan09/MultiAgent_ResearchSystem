from Agents.supervisor import supervisor_agent

state = {
    "query": "What is Agentic AI?",
    "plan": [],
    "current_plan_index": 0,
    "research_data": {},
    "summary": "",
    "fact_checked_data": {},
    "final_report": "",
    "next_step": "",
    "errors": []
}


result = supervisor_agent(state)

print("Next step:", result["next_step"])
print("Errors:", result["errors"])
