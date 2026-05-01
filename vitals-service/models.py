from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Vitals(Base):
    __tablename__ = "vitals"
    id = Column(Integer, primary_key=True,index=True)
    patient_id = Column(Integer)
    heart_rate = Column(Integer)
    spo2 = Column(Integer)
    temperature = Column(Float)