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
(fully offline mock layer – production-ready architecture – easy LLM upgrade path)

Showcases:

- Clean layered architecture & service abstraction  
- Mock AI with keyword intent detection (refund, delivery, login, complaint…)  
- Structured logging + correlation IDs  
- Pydantic-powered config & validation  
- Docker multi-stage build + compose support  
- Automatic Swagger/ReDoc documentation  

Ideal for:  
→ learning enterprise FastAPI patterns  
→ AI-integrated backend portfolio projects  
→ prototyping real customer support agents without API costs  


---

## ✨ Key Features

- REST API built with **FastAPI** (automatic OpenAPI/Swagger docs)
- Clean layered architecture (`routes` → `services` → `utils`)
- **Mocked AI engine** using keyword-based intent detection — **zero external dependencies**
- Service abstraction layer — **easy to swap mock → real LLM** (OpenAI, Azure, Anthropic, Gemini…)
- Structured logging with correlation IDs
- Type-safe configuration via **Pydantic Settings**
- Multi-stage **Dockerfile** + **docker-compose** support
- Ready for future extensions: auth, persistence, conversation memory

---

## 📸 Demo / Screenshots

Real screenshots captured from a local run of the project (no mockups).

## 📸 Demo / Screenshots

Here are real screenshots from running the project locally.

### demo1

![Swagger UI](screenshots/demo1.png)

### demo2  
  
![POST request](screenshots/demo2.png)

### demo3 
  
![API response](screenshots/demo3.png)

### demo4  
  
![Terminal logs](screenshots/demo4.png)

### demo5
 
![Docker run](screenshots/demo5.png)




## 📁 Project Structure

```
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

---


---

## 🛠 Tech Stack

| Layer                | Technology               | Purpose                              |
|----------------------|--------------------------|--------------------------------------|
| Framework            | FastAPI                  | Async API, auto docs, validation     |
| Server               | Uvicorn                  | Production-grade ASGI server         |
| Validation/Settings  | Pydantic v2              | Type-safe models & config            |
| Logging              | Python logging           | Structured + correlation IDs         |
| Containerization     | Docker & Docker Compose  | Consistent dev → prod environments   |
| Language             | Python 3.10+             | Modern syntax & performance          |

---

## 🚀 Quick Start (Local Development)

```bash
# 1. Clone the repository
git clone https://github.com/Biradarmahadev/Generative-AI-Support-Assistant-Backend.git
cd ai-support-backend

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Linux / macOS
# venv\Scripts\activate           # Windows cmd
# source venv/Scripts/activate    # Windows Git Bash

# 3. Install dependencies
pip install -r requirements.txt

# 4. (optional) Copy example env file
cp .env.example .env

# 5. Start the server (auto-reload enabled)
uvicorn app.main:app --reload --port 8000

## ⚙️ Setup & Installation (Local)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Biradarmahadev/Generative-AI-Support-Assistant-Backend.git
cd ai-support-backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn app.main:app --reload --port 8000
```

---

## 🔍 API Documentation

FastAPI automatically generates interactive API documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Usage

### POST `/api/support`

**Request Body**

```json
{
  "message": "I want a refund"
}
```

**Response**

```json
{
  "response": "Sure! Please share your order ID to process your refund."
}
```

---

## 🤖 AI Service (Mocked)

The AI service uses **keyword-based intent detection** to simulate Generative AI behavior:

* Detects user intent (refund, delivery, login)
* Returns contextual responses
* Works fully offline

🔁 The mock service can be replaced with real LLM APIs without changing the API layer.

---

## 🐳 Docker Support

### Build Image

```bash
docker build -t ai-support-backend .
```

### Run Container

```bash
docker run -p 8000:8000 ai-support-backend
```

### Docker Compose

```bash
docker-compose up --build
```

---

## 📸 Screenshots

The `screenshots/` directory contains:

* Swagger UI interface
* API request and response samples
* Terminal logs
* Docker container execution

These demonstrate the working backend and API responses.

---

## 🔐 Environment Variables

Create a `.env` file using the template below:

```env
APP_NAME=AI Support Assistant Backend
ENV=development
```

---

## 📈 Future Enhancements

* Integrate real Generative AI APIs (OpenAI / Azure OpenAI)
* Add JWT-based authentication
* Persist chat history using a database
* Add CI/CD pipeline
* Implement async background tasks

---

## 👤 Author

**Mahadev**
Backend Developer | Python | FastAPI | AI-Integrated Systems

---

## 📄 License

This project is intended for learning, portfolio, and demonstration purposes.
