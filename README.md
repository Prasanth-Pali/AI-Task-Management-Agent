# 🤖 AI Task Management Agent

An AI-powered task management application that allows users to manage tasks using natural language. Built with Python, LangChain, FastAPI, Groq LLM, and Microsoft SQL Server.

The application combines the reasoning capabilities of an LLM with real API operations, allowing the AI agent to retrieve, analyze, create, update, and delete task records.

## ✨ Features

- 💬 **Natural Language Interaction** — Ask questions about tasks using everyday English.
- 🧠 **LLM-Powered Reasoning** — Uses a Groq-hosted language model to understand user requests.
- 🛠️ **AI Tool Calling** — Uses LangChain tools to connect the LLM to application APIs.
- 📋 **Task Retrieval** — Retrieve tasks and filter results by status.
- ➕ **Create Tasks** — Create tasks through API operations.
- ✏️ **Update Tasks** — Update task details and statuses.
- 🗑️ **Delete Tasks** — Delete tasks by ID.
- 🔗 **REST API Integration** — FastAPI provides endpoints for task operations.
- 🗄️ **Database Integration** — SQLAlchemy connects Python to SQL Server.
- 🛡️ **Environment-Based Configuration** — Store API keys and sensitive configuration outside source code.

## 🏗️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application and agent logic |
| LangChain | Agent creation and tool calling |
| Groq LLM | Natural language understanding and response generation |
| FastAPI | REST API development |
| SQLAlchemy | Database connectivity and ORM |
| Microsoft SQL Server | Task data storage |
| Pydantic | Request validation and data schemas |
| Requests | HTTP communication between tools and API |
| Uvicorn | ASGI application server |
| python-dotenv | Load environment variables |

## 🔄 Architecture

```text
User
  |
  v
LangChain Agent
  |
  v
Groq LLM
  |
  v
Selects an Appropriate Tool
  |
  v
Python @tool Function
  |
  v
FastAPI REST API
  |
  v
SQLAlchemy
  |
  v
Microsoft SQL Server
  |
  v
API Result -> Agent -> Natural Language Response
```

The LLM interprets the request and decides which tool to use. The tools call the backend API, which accesses the database. The LLM then explains the returned results.

## 📁 Project Structure

```text
AI-Task-Management-Agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   └── tools.py
│
├── agent.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: Adjust the agent filename or file list if your actual project structure differs.*

## ⚙️ Prerequisites

Install or configure the following before running the application:

- Python 3.11 or a compatible version supported by your dependencies.
- Microsoft SQL Server.
- SQL Server ODBC Driver 18.
- A Groq API key.
- Git.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Prasanth-Pali/AI-Task-Management-Agent.git
cd AI-Task-Management-Agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root using `.env.example` as a template.

```dotenv
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own API key. Never commit your real `.env` file to GitHub.

### 5. Configure the database

Create or configure the `AITaskAssistantDB` database and the required `Tasks` table in Microsoft SQL Server.

Update the database connection settings in `app/database.py` to match your local SQL Server instance.

The application uses a database-first approach: the existing database schema is the source of truth, and the SQLAlchemy model is generated from that schema.

### 6. Start the FastAPI server

Open a terminal in the project root:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

### 7. Run the AI agent

Keep the FastAPI server running. Open a second terminal, activate the virtual environment, and run:

```bash
python agent.py
```

Replace `agent.py` with your actual agent filename if it differs.

## 🔌 REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks` | Retrieve all tasks |
| GET | `/api/tasks/{task_id}` | Retrieve a task by ID |
| POST | `/api/tasks` | Create a task |
| PATCH | `/api/tasks/{task_id}` | Partially update a task |
| DELETE | `/api/tasks/{task_id}` | Delete a task |

A `PUT /api/tasks/{task_id}` endpoint may also be available if full task replacement is retained in your implementation.

### Example: Create a Task

**POST** `/api/tasks`

```json
{
  "title": "Learn LangChain",
  "description": "Understand agents and tool calling",
  "dueDateUtc": "2026-10-30T12:00:00",
  "status": "Pending"
}
```

Valid task statuses:

- `Pending`
- `InProgress`
- `Completed`

## 💡 Example AI Requests

The agent is designed to understand requests such as:

- "Show me all tasks."
- "Give me the tasks whose status is Completed."
- "Show me the details of task 1."
- "Create a task to learn Azure."
- "Mark task 3 as Completed."
- "Change the title of task 2."
- "Delete task 5."

For task-related answers, the agent should use the appropriate retrieval tool to obtain real records rather than inventing task information.

## 🔐 Security Considerations

- Store API keys in environment variables.
- Never commit `.env`, database credentials, or other secrets.
- Add `.env` and `.venv/` to `.gitignore`.
- Validate all incoming API requests.
- Handle API failures and database errors safely.
- Require authorization and authentication before exposing the application beyond local development.
- Protect destructive operations such as task deletion.

## 🛣️ Future Enhancements

- Angular-based chat interface.
- User authentication and role-based access control.
- Due-date reminders and overdue task detection.
- Conversation memory.
- Retrieval-Augmented Generation (RAG) for task documentation.
- Docker-based deployment.
- Automated testing and CI/CD with GitHub Actions.
- Azure deployment and monitoring.

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- LLM integration using Groq.
- LangChain agents and custom tools.
- AI-to-REST API integration.
- FastAPI application development.
- SQL Server database access with SQLAlchemy.
- Request validation and error handling.
- Secure environment configuration.
- Git and GitHub workflow.

## 👨‍💻 Author

**Prasanth Pali**

GitHub: [Prasanth-Pali](https://github.com/Prasanth-Pali)

---

*Built as a practical project to explore AI agents, tool calling, and real-world backend integration.*
