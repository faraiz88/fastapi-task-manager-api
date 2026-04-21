from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db
from security import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


#➕ Create a new task
@router.post("/", response_model=schemas.TaskResponse)
def create(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.create_task(db, task, current_user.id)


# 📄 Get all tasks
@router.get("/", response_model=list[schemas.TaskResponse])
def read_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.get_tasks(db, current_user.id)


# 🔍 Get a single task by ID
@router.get("/{task_id}", response_model=schemas.TaskResponse)
def read_one(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    task = crud.get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# 🔁 Full update (replace entire task)
@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update(
    task_id: int,
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    updated = crud.update_task(db, task_id, task, current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


# ✏️ Partial update (modify specific fields only)
@router.patch("/{task_id}", response_model=schemas.TaskResponse)
def update_partial(
    task_id: int,
    task: schemas.TaskUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    updated = crud.update_task_partial(db, task_id, task, current_user.id)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


# ❌ Delete a task
@router.delete("/{task_id}")
def delete(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    deleted = crud.delete_task(db, task_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

