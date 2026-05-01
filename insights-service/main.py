from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base, Alert

app = FastAPI() 
Base.metadata.create_all(bind=engine)

#make a call to fastAPI endpoint to get the alerts from the database
@app.get("/alerts")
def get_alerts():
    db = SessionLocal()
    return db.query(Alert).all()