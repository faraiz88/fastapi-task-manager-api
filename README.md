FastAPI Task Manager API

A backend REST API built with FastAPI that provides user authentication and task management features using a PostgreSQL database.

🚀 Features
User registration and login (JWT authentication)
Secure password hashing
Create, read, update, and delete tasks (CRUD)
User-specific task management
PostgreSQL database integration
Input validation using Pydantic

🛠 Tech Stack
FastAPI – API framework
SQLAlchemy – ORM for database operations
PostgreSQL – Database
Pydantic – Data validation
Passlib & Bcrypt – Password hashing
Python-JOSE – JWT authentication

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/faraiz88/fastapi-task-manager-api.git
cd fastapi-task-manager-api
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file:
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
5. Run the server
uvicorn main:app --reload


📌 API Documentation
After running the server, access:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc


👤 Author
Mohammed Faraiz
