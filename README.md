
<div align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=36&pause=1000&color=6A5ACD&center=true&vCenter=true&width=700&lines=Generative+AI+Support+Assistant;FastAPI+Backend+with+Mock+LLM;Built+for+Real-World+AI+Support" alt="Typing SVG Banner">
  <br><br>

  <img src="https://img.shields.io/badge/Made%20with-FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/LLM%20Mock-Offline%20%26%20Free-00C4B4?style=for-the-badge" />

  <br><br>
  <strong>Production-style • Modular • AI-ready • Dockerized</strong>
</div>

<br>

# Generative AI Support Assistant Backend

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-brightgreen.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Modern FastAPI backend simulating intelligent customer support powered by generative AI**  
(fully offline mock layer – production-ready architecture – easy path to real LLM)

Showcases:
- Clean layered architecture & service abstraction
- Mock AI with keyword intent detection (refund, delivery, login, complaint…)
- Structured logging + correlation IDs
- Pydantic-powered config & validation
- Docker multi-stage build + compose support
- Automatic Swagger/ReDoc documentation

Ideal for:
- Learning enterprise FastAPI patterns
- AI-integrated backend portfolio projects
- Prototyping real customer support agents without API costs

## ✨ Key Features

- REST API built with **FastAPI** (automatic OpenAPI/Swagger docs)
- Clean layered architecture (`routes` → `services` → `utils`)
- **Mocked AI engine** using keyword-based intent detection — **zero external dependencies**
- Service abstraction layer — **easy to swap mock → real LLM** (OpenAI, Azure, Anthropic, Gemini…)
- Structured logging with correlation IDs
- Type-safe configuration via **Pydantic Settings**
- Multi-stage **Dockerfile** + **docker-compose** support
- Ready for future extensions: auth, persistence, conversation memory

## 🏗 Modern Architecture Overview 

```mermaid
graph TD
    %% Styling for dark/light mode compatibility
    classDef frontend fill:#0d1117,stroke:#58a6ff,stroke-width:2px,color:#c9d1d9,rx:8px,ry:8px
    classDef api fill:#21262d,stroke:#f78166,stroke-width:2px,color:#f0f6fc,rx:8px,ry:8px
    classDef llm fill:#2ea44f,stroke:#2ea44f,stroke-width:2px,color:#fff,rx:8px,ry:8px
    classDef db fill:#444d56,stroke:#6e7681,stroke-width:2px,color:#c9d1d9,rx:8px,ry:8px
    classDef cache fill:#d18616,stroke:#d18616,stroke-width:2px,color:#fff,rx:8px,ry:8px
    classDef queue fill:#b392f0,stroke:#b392f0,stroke-width:2px,color:#fff,rx:8px,ry:8px
    classDef infra fill:#30363d,stroke:#8b949e,stroke-width:2px,color:#c9d1d9,rx:8px,ry:8px
    classDef legend fill:#161b22,stroke:#30363d,stroke-width:1px,color:#8b949e

    %% Main user flow
    A[User<br>Web / Mobile / Slack / Teams / WhatsApp]:::frontend
    A -->|HTTP / WebSocket / gRPC| B[API Gateway<br>Auth • Rate Limit • CORS • Logging]:::api

    subgraph "Core Backend Layer"
        B --> C[FastAPI / NestJS / Django Ninja<br>Async APIs • Streaming Responses]:::api
        C --> D[Conversation Manager<br>Session • Context • Memory • History]:::api
        C --> E[Prompt Engineering & Guardrails<br>System Prompts • RAG • Tool Calls • Safety]:::api
    end

    D --> F[(Vector DB / Knowledge Store<br>Pinecone • Weaviate • PGVector • Qdrant)]:::db
    D --> G[(Redis / Valkey<br>Session Cache • Rate Limits • Pub/Sub)]:::cache

    subgraph "Generative AI Core"
        E --> H[LLM Router & Orchestrator<br>OpenAI • Anthropic • Grok • Llama • Gemini • Mistral]:::llm
        H -->|Function / Tool Calling| I[Tools & Agents<br>Web Search • DB Query • Math • Calendar • Code Exec]:::api
        H -->|Retrieval Augmented Generation| F
    end

    subgraph "Async Processing"
        C -->|Celery / RQ / Background Tasks| J[Task Queue<br>Notifications • Email • Slack • Analytics]:::queue
    end

    subgraph "Infrastructure & Observability"
        K[Cloud / Hosting<br>AWS • GCP • Azure • Railway • Fly.io • Render]:::infra
        L[Observability Stack<br>Langfuse • Prometheus • Grafana • Sentry • Loki]:::infra
        M[CI/CD & Infra<br>GitHub Actions • Docker • Terraform • Helm]:::infra
    end

    %% Infrastructure connections (dotted lines)
    B ~~~ K
    C ~~~ K
    H ~~~ K
    J ~~~ K
    C --> L
    H --> L
    C ~~~ M

    %% Legend at bottom
    Legend[Legend ────────────────────────────────────────<br>→ Synchronous / HTTP<br>⇒ Streaming / WebSocket<br>→ Background / Async]:::legend

    style Legend text-align:left
```

## 📁 Project Structure

```text
ai-support-backend/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app entry point
│   ├── config.py             # Typed environment settings
│   ├── routes/
│   │   ├── __init__.py
│   │   └── support.py        # /api/support endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   └── ai_service.py     # Mock AI intent classifier
│   └── utils/
│       ├── __init__.py
│       └── logger.py         # Logging configuration
├── screenshots/              # Demo screenshots
│   ├── swagger-ui.png
│   ├── post-request.png
│   ├── api-response.png
│   ├── terminal-logs.png
│   └── docker-run.png
├── .env.example
├── .gitignore
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🛠 Tech Stack

| Layer              | Technology                  | Purpose                                      |
|--------------------|-----------------------------|----------------------------------------------|
| Framework          | FastAPI                     | Async API, auto docs, validation             |
| Server             | Uvicorn                     | Production-grade ASGI server                 |
| Validation/Settings| Pydantic v2                 | Type-safe models & config                    |
| Logging            | Python logging              | Structured + correlation IDs                 |
| Containerization   | Docker & Docker Compose     | Consistent dev → prod environments           |
| Language           | Python 3.10+                | Modern syntax & performance                  |

## 🚀 Quick Start (Local Development)

```bash
# 1. Clone the repository
git clone https://github.com/Biradarmahadev/Generative-AI-Support-Assistant-Backend.git
cd Generative-AI-Support-Assistant-Backend

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows cmd
# source venv/Scripts/activate    # Windows Git Bash

# 3. Install dependencies
pip install -r requirements.txt

# 4. (optional) Copy example env file
cp .env.example .env

# 5. Start the server (auto-reload enabled)
uvicorn app.main:app --reload --port 8000
```

API Documentation:  
→ http://127.0.0.1:8000/docs (Swagger UI)  
→ http://127.0.0.1:8000/redoc (ReDoc)

## 📌 API Usage Example

**POST** `/api/support`

**Request Body**
```json
{
  "message": "I want a refund for my order"
}
```

**Response**
```json
{
  "response": "Sure! Please share your order ID to process your refund request."
}
```

## 🤖 AI Service (Mocked – Offline & Free)

The AI layer uses **keyword-based intent detection** to simulate generative behavior:

- Detects intents: refund, delivery status, login issue, complaint, order tracking…
- Returns contextual, helpful responses
- No external API calls → zero cost & fully offline
- Designed for **easy upgrade** → replace mock with real LLM (OpenAI, Grok, Llama, etc.)

## 🐳 Docker Support

### Build & Run Single Container

```bash
docker build -t ai-support-backend .
docker run -p 8000:8000 ai-support-backend
```

### Using Docker Compose

```bash
docker-compose up --build
```

## 📸 Screenshots

Check the `screenshots/` folder for visuals:
- Swagger UI interface
- Sample API request/response
- Terminal logs with correlation IDs
- Docker container running

## 🔐 Environment Variables (.env)

```env
APP_NAME=AI Support Assistant Backend
ENV=development
LOG_LEVEL=INFO
```

## 📈 Future Enhancements

- Real LLM integration (OpenAI / Grok / Llama / Gemini)
- JWT authentication & user sessions
- Persistent chat history (PostgreSQL / MongoDB)
- RAG support with vector database
- Rate limiting & API security
- CI/CD pipeline (GitHub Actions)

## 👤 Author

**Mahadev**  
Backend Developer | Python | FastAPI | AI-Integrated Systems | Bengaluru

## 📄 License

MIT License – feel free to use, modify, and learn from this project!

<div align="center">
  <br/>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer&text=Thanks%20for%20Visiting%20✨&fontSize=30&fontColor=fff&animation=twinkling" alt="Waving footer"/>
</div>
```


