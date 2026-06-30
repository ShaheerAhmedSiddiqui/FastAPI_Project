from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql+psycopg2://postgres:data123@localhost:5432/inventorySys"
engine = create_engine(db_url)
SessionLocal  = sessionmaker(autocommit = False, autoflush=False, bind=engine)