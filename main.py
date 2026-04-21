from fastapi import FastAPI, Depends
from database import engine, Base, get_db
from routers import tasks, auth
from sqlalchemy.orm import Session
import models

app = FastAPI()

app.include_router(tasks.router)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "API is working"}


