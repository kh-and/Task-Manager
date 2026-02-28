from sqlalchemy.orm import Session
from app import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, password_hash=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user