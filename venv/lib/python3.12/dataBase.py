from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:////home/mac/Programs/Python/uteChat/venv/lib/python3.12/uutah.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)

init_db()

# Usage example: 
# 1. Call init_db() once to initialize the database schema
# 2. Use SessionLocal to interact with the database





