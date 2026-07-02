from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Schemas.user import Login_User, UserCreate, UserResponse
from database import get_db
from Schemas import token
from models.user import User
from utils import security

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = security.hash_password(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/login", response_model=UserResponse)
def login_user(user: Login_User, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="User not found")
    if not security.verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return existing_user
    