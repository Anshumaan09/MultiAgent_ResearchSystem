import streamlit as st

from Graph.workflow import build_graph


# Build the workflow once
workflow = build_graph()


st.set_page_config( page_title="Multi-Agent Research System", page_icon="🤖", layout="wide")


st.title("🤖 Multi-Agent Research System")

with st.expander("🔄 Actual LangGraph Workflow"):
    st.code(        """
START
  ↓
Supervisor
  ↓
Planner
  ↓
Supervisor
  ↓
Research
  ↓
Supervisor
  ↓
Fact Checker
  ↓
Supervisor
  ↓
Summary
  ↓
Supervisor
  ↓
Writer
  ↓
Supervisor
  ↓
END
""",        language="text",    )

st.markdown( """
Enter any research topic and the system will:

- 🧠 Plan the research
- 🌐 Search the web using Tavily
- 🔍 Verify the information
- 📝 Generate a technical summary
- 📄 Produce a professional research report
""")


query = st.text_input( "Enter your research topic:", placeholder="e.g., What is Agentic AI?")


if st.button("Generate Report", type="primary"):
    if not query.strip():
        st.warning("Please enter a research topic.")
    else:
        initial_state = {
            "query": query,
            "plan": [],
            "current_plan_index": 0,
            "research_data": {},
            "summary": "",
            "fact_checked_data": {},
            "final_report": "",
            "next_step": "",
            "errors": [],
        }

        with st.spinner("Running multi-agent workflow..."):
            result = workflow.invoke(initial_state)

        if result["errors"]:
            st.error("Workflow completed with errors.")

            for error in result["errors"]:
                st.write(f"**{error['agent']}**: {error['message']}")

        else:
            st.success("Report generated successfully!")

            st.markdown(result["final_report"])

            st.download_button( label="📥 Download Report", data=result["final_report"], file_name="research_report.md", mime="text/markdown")
