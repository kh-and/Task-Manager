from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)