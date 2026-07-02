import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE_URL = os.getenv("DATABASE_URL")


DATABASE_URL = "postgresql://postgres:Admin123@localhost:5432/student_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from models import company as company_model, job as job_model, user as user_model

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()