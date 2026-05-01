from kafka import KafkaConsumer
from database import SessionLocal, engine
from models import Base, Alert
import json

Base.metadata.create_all(bind=engine)

consumer = KafkaConsumer(
    "patient-vitals",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="insights-group"
)

print("Listening...")

for msg in consumer:
    data = msg.value

    if data["heart_rate"] > 100:
        db = SessionLocal()

        alert = Alert(
            patient_id=data["patient_id"],
            message="High heart rate detected"
        )

        db.add(alert)
        db.commit()

        print("Alert saved")