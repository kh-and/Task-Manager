from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from app import models, schemas
from passlib.context import CryptContext
from . import models, schemas

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, password_hash=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, user_id: int, completed: bool | None = None, limit: int = 10, offset: int = 0, order: str = "desc"):

    query = db.query(models.Task).filter(models.Task.owner_id == user_id)

    if completed is not None:
        query = query.filter(models.Task.completed == completed)

    if order == "desc":
        query = query.order_by(desc(models.Task.created_at))
    else:
        query = query.order_by(asc(models.Task.created_at))

    total = query.count()

    tasks = query.offset(offset).limit(limit).all()

    return {
        "total": total,
        "items": tasks
    }

def update_task(db: Session, db_task, task_update: schemas.TaskUpdate):
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, db_task):
    db.delete(db_task)
    db.commit()
    return