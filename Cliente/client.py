import os
import random
import time
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")

while True:
    data = {"device_id": "sensor_01", "val": round(random.uniform(20.0, 30.0), 2)}
    try:
        res = requests.post(f"{API_URL}/telemetry", json=data, timeout=3)
        print(f"Enviado: {data} -> Respuesta: {res.status_code}")
    except Exception as e:
        print(f"Error conectando: {e}")
    time.sleep(2)