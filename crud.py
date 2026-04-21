from sqlalchemy.orm import Session
from security import hash_password
import models, schemas


def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    new_task = models.Task(**task.model_dump(), owner_id=user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_tasks(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(
        models.Task.id == task_id,
        models.Task.owner_id == user_id
    ).first()


def update_task(db: Session, task_id: int, task: schemas.TaskCreate, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if not db_task:
        return None
    db_task.title = task.title
    db_task.description = task.description
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task_partial(db: Session, task_id: int, task: schemas.TaskUpdate, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if not db_task:
        return None
    update_data = task.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task


def create_user(db, user):
    hashed = hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db, email: str):
    return db.query(models.User).filter(models.User.email == email).first()