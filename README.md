 🎮 Choose Your Own Adventure AI

A full-stack AI-powered interactive storytelling app built with **FastAPI**, **Python**, and **React**. Users enter a theme and the AI generates a branching narrative — demonstrating end-to-end product engineering across backend, database, and frontend layers.

---

 🚀 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · FastAPI · SQLAlchemy |
| AI | Anthropic / OpenAI API |
| Frontend | React · React Router Dom |
| Database | SQLite / PostgreSQL |
| Deployment | Choreo (free tier) |

---
 ✨ Features

- **AI Story Generation** — dynamic branching narratives via LLM integration
- **RESTful API Design** — structured routers, Pydantic schemas, and clean separation of concerns
- **Persistent Storage** — database models with full CRUD via SQLAlchemy ORM
- **Component-Based UI** — reusable React components with client-side routing
- **Environment Config** — secure secrets management with `.env` and config modules
- **Free Cloud Deployment** — live demo hosted on Choreo

---

 🛠 Setup

```bash
 Backend
uv venv && uv pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
npm install && npm run dev
```

Add your API key to `.env`:
```
AI_API_KEY=your_key_here
```

---

## 📁 Project Structure

```
backend/   → FastAPI app · routers · models · schemas
frontend/  → React components · pages · styles
```

---

## 🌐 Live Demo

Deployed via [Choreo](https://choreo.dev) — view the live app [here](#).

---

## 📄 License

MIT
