# FastAPI Task Manager API

A production-ready backend REST API built with FastAPI that provides JWT authentication and task management using PostgreSQL.

---

## 🚀 Features

- User registration and login
- JWT authentication & authorization
- Secure password hashing with bcrypt
- Full CRUD operations for tasks
- User-specific task management
- PostgreSQL database integration
- Input validation using Pydantic
- Interactive API documentation with Swagger UI
- Cloud deployment on Render

---

## 🛠 Tech Stack

- FastAPI — API framework
- SQLAlchemy — ORM
- PostgreSQL — Database
- Pydantic — Data validation
- Passlib & Bcrypt — Password hashing
- Python-JOSE — JWT authentication
- Render — Cloud deployment platform

---

## 🌐 Live Deployment

### Live API
```text
https://fastapi-task-manager-api-cb58.onrender.com/
```

### Swagger Documentation
```text
https://fastapi-task-manager-api-cb58.onrender.com/docs
```

---

## ⚙️ Local Setup Instructions

### Clone the repository

```bash
git clone https://github.com/faraiz88/FastAPI-Task-Manager-API.git
cd FastAPI-Task-Manager-API
```

---

### Create virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### Run the server

```bash
uvicorn main:app --reload
```

Server runs at:

```text
http://127.0.0.1:8000
```

---

## 📌 API Documentation (Local)

- Swagger UI:
```text
http://127.0.0.1:8000/docs
```

- ReDoc:
```text
http://127.0.0.1:8000/redoc
```

---

## 🔐 Authentication

This project uses JWT Bearer Authentication.

### Login Flow

1. Register a user
2. Login using email and password
3. Copy the access token
4. Click the **Authorize** button in Swagger UI
5. Paste the token to access protected routes

---

## 📂 Project Structure

```text
.
├── routers/
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── security.py
├── requirements.txt
└── .env
```

---

## 👤 Author

Mohammed Faraiz
