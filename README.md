# healthcare-event-platform

workflow:

user makes post request through api call -> vitals service (FastAPI) -> (1) store patient data to database (SQLite) and (2) send event to Kafka
from (2) -> insights service (analytics) -> send alert or insights (usually through get request)
