from Agents.planner import planner_agent

state = {
    "query": "Agentic AI",
    "plan": [],
    "current_plan_index": 0,
    "research_data": {},
    "summary_data": {},
    "fact_checked_data": {},
    "final_report": "",
    "errors": []
}

updated_state = planner_agent(state)

assert len(updated_state["plan"]) == 5
assert updated_state["errors"] == []

for item in updated_state["plan"]:
    assert "id" in item
    assert "section" in item
    assert "objective" in item