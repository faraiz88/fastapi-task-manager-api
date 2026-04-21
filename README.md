# FastAPI Task Manager API

A backend REST API built with FastAPI that provides user authentication and task management using a PostgreSQL database.

---

## 🚀 Features

* User registration and login (JWT authentication)
* Secure password hashing
* Create, read, update, and delete tasks (CRUD)
* User-specific task management
* PostgreSQL database integration
* Input validation using Pydantic

---

## 🛠 Tech Stack

* FastAPI – API framework
* SQLAlchemy – ORM
* PostgreSQL – Database
* Pydantic – Data validation
* Passlib & Bcrypt – Password hashing
* Python-JOSE – JWT authentication

---

## ⚙️ Setup Instructions

### Clone the repository

```bash
git clone https://github.com/faraiz88/fastapi-task-manager-api.git
cd fastapi-task-manager-api
```

### Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
```

### Run the server

```bash
uvicorn main:app --reload
```

---

## 📌 API Documentation

* http://127.0.0.1:8000/docs
* http://127.0.0.1:8000/redoc

---

## 👤 Author

Mohammed Faraiz
