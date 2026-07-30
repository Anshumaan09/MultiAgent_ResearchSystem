# Multi-Agent Research System

A **Supervisor-Orchestrated Multi-Agent Research System** built with **LangGraph**, **LangChain**, **Groq**, and **Tavily**. The system performs **live web-grounded research**, **fact checking**, **summarization**, and **professional report generation** using a team of specialized AI agents coordinated by a dynamic supervisor.

---

## Features

* **Supervisor-driven orchestration** using LangGraph conditional routing
* **Dynamic execution flow** instead of a fixed linear pipeline
* **Live web search** using Tavily
* **Planner Agent** for research decomposition
* **Research Agent** for web-grounded information synthesis
* **Fact Checker Agent** for content verification
* **Summary Agent** for concise technical summaries
* **Writer Agent** for professional Markdown report generation
* **Typed shared state** using `TypedDict`
* **Modular prompt architecture**
* **Unit and integration tests**

---

## Actual LangGraph Workflow

Unlike a traditional sequential pipeline, this project uses a **Supervisor Agent** that examines the shared state after every step and dynamically decides which agent should execute next.

```text
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
```

### Research Execution

```text
User Query
      ↓
Supervisor
      ↓
Planner
      ↓
Research Agent
      ├── Tavily Web Search
      ├── Real-Time Web Results
      └── LLM Synthesis
      ↓
Fact Checker
      ↓
Summary
      ↓
Writer
      ↓
Professional Markdown Report
```

This makes the system **state-driven and adaptive**, demonstrating **true LangGraph conditional routing** rather than a simple hardcoded chain.

---

## Project Structure

```text
MultiAgent_Research_System/
│
├── app.py
├── src/
│   ├── Agents/
│   │   ├── planner.py
│   │   ├── Researcher.py
│   │   ├── fact_checker.py
│   │   ├── summary.py
│   │   ├── writer.py
│   │   └── supervisor.py
│   │
│   ├── Graph/
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── Prompts/
│   │   ├── planner_prompt.py
│   │   ├── research_prompt.py
│   │   ├── fact_checker_prompt.py
│   │   ├── summarizer_prompt.py
│   │   └── writer_prompt.py
│   │
│   ├── Utils/
│   │   ├── llm_response.py
│   │   ├── document_builder.py
│   │   └── web_search.py
│   │
│   ├── config.py
│   └── llm.py
│
├── Tests/
├── README.md
└── pyproject.toml
```

---

## Tech Stack

| Technology       | Purpose                        |
| ---------------- | ------------------------------ |
| **Python 3.12+** | Core language                  |
| **LangGraph**    | Dynamic workflow orchestration |
| **LangChain**    | LLM integration                |
| **Groq**         | High-speed LLM inference       |
| **Tavily**       | Live web search                |
| **TypedDict**    | Shared workflow state          |
| **Streamlit**    | Frontend UI                    |

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/MultiAgent_Research_System.git
cd MultiAgent_Research_System
```

### Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows (CMD)**

```cmd
.venv\Scripts\activate
```

### Install dependencies

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a **`.env`** file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run the Streamlit Frontend

```cmd
set PYTHONPATH=src && streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## Run the Full Workflow

```cmd
set PYTHONPATH=src && python Tests\test_workflow.py
```

Example:

```text
Enter your research topic: What is Agentic AI?
```

---

## Example Output

The system generates a structured report such as:

```markdown
# Technical Research Report: Agentic AI

## Executive Summary
...

## Introduction
...

## Core Principles
...

## Technical Implementation
...

## Applications
...

## Conclusion
...
```

---

## Shared State

```python
class ResearchState(TypedDict):
    query: str
    plan: list[PlanItem]
    current_plan_index: int
    research_data: dict[str, str]
    fact_checked_data: dict[str, str]
    summary: str
    final_report: str
    next_step: str
    errors: list[ErrorInfo]
```

The `next_step` field is used by the **Supervisor Agent** to perform **conditional routing** in LangGraph.

---

## What This Project Demonstrates

* **Supervisor-based orchestration**
* **Stateful multi-agent coordination**
* **LangGraph conditional edges**
* **Live Tavily-powered web retrieval**
* **RAG-style grounded research generation**
* **Professional report generation pipeline**
* **Reusable utility and prompt modules**
* **Integration testing for multi-agent workflows**

---

## Future Improvements

* Source citations in the final report
* Parallel research execution
* Human-in-the-loop approval
* Retry and recovery strategies
* Persistent memory
* FastAPI deployment
* PDF and DOCX export
* LLM-based intelligent supervisor

---

## Author

**Anshumaan Panigrahi**

Built as a hands-on exploration of **Agentic AI, LangGraph orchestration, live web-grounded research, and supervisor-driven multi-agent system design**.
