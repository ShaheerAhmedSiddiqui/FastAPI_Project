from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:data123@localhost:5432/inventorySys"
engine = create_engine()
SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)