#Sqlalchemy is a way to talk to the database in Python. It helps us create, read, update, and delete data in a database using Python code instead of writing raw SQL queries.
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./insights.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)