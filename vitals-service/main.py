from producer import publish_vitals
from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Base, Vitals as VitalsModel

app = FastAPI()
Base.metadata.create_all(bind=engine)

class VitalsRequest(BaseModel):
    patient_id: int 
    heart_rate: int
    spo2: int
    temperature: float

# temporary in-memory storage (we’ll replace with SQLAlchemy later)
#db = []

@app.post("/vitals")
def add_vitals(vitals: VitalsRequest):
    #db.append(vitals.dict())
    db = SessionLocal()

    new_vitals = VitalsModel(
        patient_id=vitals.patient_id,
        heart_rate=vitals.heart_rate,
        spo2=vitals.spo2,
        temperature=vitals.temperature
    )
    db.add(new_vitals)
    db.commit()

    publish_vitals({
    "patient_id": vitals.patient_id,
    "heart_rate": vitals.heart_rate,
    "spo2": vitals.spo2,
    "temperature": vitals.temperature
    })
    return {"message": "Vitals recorded", "data": vitals}

@app.get("/vitals")
def get_vitals():
    db = SessionLocal()
    vitals = db.query(VitalsModel).all()
    return vitals