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

## Architecture

```text
                    START
                       │
                       ▼
                Supervisor Agent
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
      Planner       Research       Writer
                       │
                       ▼
                Fact Checker
                       │
                       ▼
                    Summary
                       │
                       ▼
                     Writer
                       │
                       ▼
                Supervisor Agent
                       │
                       ▼
                      END
```

### Research Flow

```text
User Query
      ↓
Supervisor
      ↓
Planner
      ↓
Research Agent
      ├── Tavily Web Search
      ├── Web Context Retrieval
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

---

## Project Structure

```text
MultiAgent_Research_System/
│
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
│   ├── test_planner.py
│   ├── test_researcher.py
│   ├── test_factChecker.py
│   ├── test_summarizer.py
│   ├── test_writer.py
│   ├── test_supervisor.py
│   └── test_workflow.py
│
├── .env
├── pyproject.toml
└── README.md
```

---

## Tech Stack

| Technology               | Purpose                  |
| ------------------------ | ------------------------ |
| **Python 3.12+**         | Core language            |
| **LangGraph**            | Workflow orchestration   |
| **LangChain**            | LLM integration          |
| **Groq**                 | High-speed LLM inference |
| **Tavily**               | Live web search          |
| **Pydantic / TypedDict** | Typed shared state       |
| **UV / pip**             | Dependency management    |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/MultiAgent_Research_System.git
cd MultiAgent_Research_System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (CMD)**

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

Using **uv** (recommended):

```bash
uv sync
```

Or using **pip**:

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

## Running the Project

### Run the full workflow

```cmd
set PYTHONPATH=src && python Tests\test_workflow.py
```

Example:

```text
Enter your research topic: What is Agentic AI?
```

The system will generate a **professional Markdown research report**.

---

## Running Individual Agent Tests

### Planner

```cmd
set PYTHONPATH=src && python Tests\test_planner.py
```

### Research Agent

```cmd
set PYTHONPATH=src && python Tests\test_researcher.py
```

### Fact Checker

```cmd
set PYTHONPATH=src && python Tests\test_factChecker.py
```

### Summary Agent

```cmd
set PYTHONPATH=src && python Tests\test_summarizer.py
```

### Writer Agent

```cmd
set PYTHONPATH=src && python Tests\test_writer.py
```

### Supervisor Agent

```cmd
set PYTHONPATH=src && python Tests\test_supervisor.py
```

---

## Example Output

The system generates a structured report like:

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

## Shared State Design

The workflow uses a **typed shared state** passed between all agents.

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

This enables **stateful multi-agent coordination** and dynamic routing.

---

## Key Learning Outcomes

This project demonstrates:

* **LangGraph conditional routing**
* **Supervisor-based orchestration**
* **Stateful multi-agent systems**
* **Live web-grounded retrieval (RAG-style)**
* **Prompt modularization**
* **Typed workflow state management**
* **Agent communication through shared state**
* **Refactoring and reusable component design**

---

## Future Improvements

* Source citations in the final report
* Parallel research execution
* Human-in-the-loop approval
* Retry and recovery strategies
* Persistent memory
* Streamlit UI
* FastAPI deployment
* PDF and DOCX export
* LLM-based intelligent supervisor

---

## Why This Project Matters

Unlike simple LangChain chains, this project implements a **dynamic agentic architecture** where:

* execution order is determined **at runtime**,
* agents communicate through **shared state**,
* the supervisor can **adapt the workflow** based on intermediate results,
* research is grounded using **real-time web retrieval**.

This makes the system a strong demonstration of **modern Agentic AI engineering practices** using **LangGraph**.

---

## Author

**Anshumaan Panigrahi**

Built as a hands-on exploration of **Agentic AI, LangGraph orchestration, live web-grounded research, and multi-agent system design**.
