



```markdown
# Choose Your Own Adventure AI

An interactive, AI-powered Choose Your Own Adventure application featuring a modern Python FastAPI backend and a React frontend.

---

## 🛠️ Development Setup & History Log

This document records the exact terminal commands and steps executed to set up the project environment on Windows (using Git Bash / UCRT64).



### 2. Clone the Repository

Cloned the base template repository from GitHub:

```bash
git clone [https://github.com/abdoulKARENZO-max/Choose-Your-Own-Adventure-AI.git](https://github.com/abdoulKARENZO-max/Choose-Your-Own-Adventure-AI.git)

```

### 3. Environment & Tool Versions

Verified runtime environments:

* **Node.js:** `v24.21.0`
* **npm:** `v11.19.0`
* **Python:** `3.14.7`

### 4. Project Workspace Setup

Created the custom project folder structure separating the backend and frontend (`reactjs`):

```bash
mkdir My-Choose-Your-Own-Adventure-AI
cd My-Choose-Your-Own-Adventure-AI
mkdir backend reactjs

```

### 5. Backend Initialization with `uv`

Navigated into the backend folder, configured the `uv` tool path, and initialized a new Python project:

```bash
cd backend
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
uv init

```

*(Initialized project `backend`)*

### 6. Installing Backend Dependencies

Installed all required packages for FastAPI, LangChain, OpenAI integration, database management via SQLAlchemy, and PostgreSQL binary support (`psycopg2-binary`):

```bash
uv add fastapi[all] langchain langchain-openai python-dotenv sqlalchemy uvicorn psycopg2-binary

```

#### Installed Packages Summary:

* **Web & API:** `fastapi`, `uvicorn`, `starlette`, `anyio`, `httpx`
* **AI & LLM:** `langchain`, `langchain-core`, `langchain-openai`, `langgraph`, `openai`, `tiktoken`
* **Database & Utilities:** `sqlalchemy`, `psycopg2-binary`, `python-dotenv`, `pydantic`, `pydantic-settings`
* **Observability & Core Tools:** `opentelemetry-*`, `rich`, `typer`, `click`

---

## 🚀 Next Steps

1. **Configure Environment Variables:** Create a `.env` file inside the `backend/` directory and add your API keys (e.g., `OPENAI_API_KEY`).
2. **Run the Backend:** Start your FastAPI development server using `uv run uvicorn main:app --reload`.
3. **Setup Frontend:** Navigate to the `reactjs/` directory to build out your user interface.

```

```