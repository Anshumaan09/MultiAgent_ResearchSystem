# 🤖 Multi-Agent Research System

> **Supervisor-Orchestrated Agentic AI for Live Web-Grounded Technical Research**

A production-style **Agentic AI research system** built with **LangGraph**, **LangChain**, **Groq**, and **Tavily** that automatically plans research, searches the web in real time, verifies information, summarizes findings, and generates a polished **Markdown technical report**.

Unlike simple LLM chains, this project uses a **Supervisor Agent with conditional routing**, making the workflow **dynamic, stateful, and adaptive**.

---

## 🚀 What Makes This Different?

Traditional AI workflows are usually:

```text
User Query → LLM → Answer
```

This project implements a **true multi-agent architecture**:

```text
User Query
      ↓
Supervisor Agent
      ↓
Planner Agent
      ↓
Research Agent
      ├── Tavily Web Search
      ├── Live Web Context
      └── LLM Synthesis
      ↓
Fact Checker Agent
      ↓
Summary Agent
      ↓
Writer Agent
      ↓
Professional Technical Report
```

The **Supervisor Agent** continuously inspects the shared workflow state and decides which agent should execute next using **LangGraph conditional edges**.

---

# ✨ Features

### 🧠 Agentic Orchestration

* Supervisor-driven workflow execution
* Dynamic conditional routing with LangGraph
* Shared typed state across all agents

### 🌐 Live Web-Grounded Research

* Real-time web search using **Tavily**
* Web context injected into research prompts
* Reduced hallucinations through grounded generation

### 📝 Professional Report Generation

* Automatic research planning
* Structured technical summaries
* Clean Markdown report output
* Downloadable report generation

### 🛡️ Reliability

* Typed `ResearchState`
* Modular prompt architecture
* Reusable utility components
* Unit and integration tests

---

# 🏗️ System Architecture

## Actual LangGraph Execution Flow

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

This is **not a hardcoded pipeline**. The Supervisor dynamically determines the next step based on the current workflow state.

---

# 📂 Project Structure

```text
MultiAgent_Research_System/
│
├── app.py                         # Streamlit frontend
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

# 🧩 Agent Responsibilities

| Agent            | Responsibility                                      |
| ---------------- | --------------------------------------------------- |
| **Supervisor**   | Controls workflow execution and routing             |
| **Planner**      | Breaks the query into research sections             |
| **Research**     | Performs Tavily web search and synthesizes findings |
| **Fact Checker** | Reviews and validates researched content            |
| **Summary**      | Produces a concise technical summary                |
| **Writer**       | Generates the final professional Markdown report    |

---

# 🔧 Tech Stack

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| **Python 3.12+** | Core language               |
| **LangGraph**    | Dynamic agent orchestration |
| **LangChain**    | LLM integration             |
| **Groq**         | Fast LLM inference          |
| **Tavily**       | Live web search             |
| **Streamlit**    | Frontend UI                 |
| **TypedDict**    | Shared typed workflow state |

---

# ⚡ Quick Start

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/MultiAgent_Research_System.git
cd MultiAgent_Research_System
```

## 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### Windows

```cmd
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

Using **uv** (recommended):

```bash
uv sync
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# 🖥️ Run the Frontend

```cmd
set PYTHONPATH=src && streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🧪 Run the Full Workflow

```cmd
set PYTHONPATH=src && python Tests\test_workflow.py
```

Example:

```text
Enter your research topic: What is Agentic AI?
```

---

# 📊 Example Output

The system generates a structured technical report such as:

```markdown
# Technical Research Report: Agentic AI

## Executive Summary
...

## Introduction to Agentic AI
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

# 🧠 Shared Workflow State

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

The `next_step` field enables **Supervisor-based conditional routing**.

---

# 🔍 Tavily Web Search Integration

The Research Agent uses **live web retrieval**:

```python
web_context = search_web(
    query=f"{topic} - {objective}"
)
```

This allows the system to:

* fetch **current information from the web**,
* ground research in **real sources**,
* synthesize findings into structured technical content.

---

# 🧪 Testing

Run individual agent tests:

```cmd
set PYTHONPATH=src && python Tests\test_planner.py
set PYTHONPATH=src && python Tests\test_researcher.py
set PYTHONPATH=src && python Tests\test_factChecker.py
set PYTHONPATH=src && python Tests\test_summarizer.py
set PYTHONPATH=src && python Tests\test_writer.py
set PYTHONPATH=src && python Tests\test_supervisor.py
```

---

# 🎯 Key Engineering Concepts Demonstrated

This project showcases:

* ✅ **LangGraph conditional routing**
* ✅ **Supervisor-based orchestration**
* ✅ **Stateful multi-agent coordination**
* ✅ **RAG-style live web retrieval**
* ✅ **Prompt modularization**
* ✅ **Reusable utility components**
* ✅ **Refactoring and separation of concerns**
* ✅ **Integration testing for agentic workflows**

---

# 📈 Future Improvements

* 📚 Source citations in the final report
* ⚡ Parallel research execution
* 👤 Human-in-the-loop approval
* 🔁 Retry and recovery strategies
* 🧠 Persistent memory
* 🌍 FastAPI deployment
* 📄 PDF / DOCX export
* 🤖 LLM-driven intelligent supervisor
* 📡 Streaming intermediate agent outputs

---

# 🏆 Why This Project Matters

Most LangChain projects demonstrate **sequential chains**.

This project demonstrates:

* **dynamic agent orchestration**,
* **shared workflow state**,
* **conditional execution loops**,
* **live web-grounded reasoning**,
* **professional report generation**, and
* **supervisor-controlled adaptive workflows**.

It is a strong portfolio example of **modern Agentic AI engineering with LangGraph**.

---

# 👨‍💻 Author

### **Anshumaan Panigrahi**

Built as a hands-on exploration of:

* **Agentic AI**
* **LangGraph orchestration**
* **Supervisor-driven workflows**
* **Live web-grounded research**
* **Multi-agent system design**
* **Stateful AI application architecture**

---

# ⭐ If You Found This Interesting

If this project helped you understand **LangGraph, Supervisor Agents, Tavily integration, or Agentic AI workflows**, consider giving the repository a **⭐ star** and sharing it with other developers exploring **stateful multi-agent systems**. 🚀
