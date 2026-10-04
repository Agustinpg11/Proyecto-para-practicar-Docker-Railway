import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
DB_FILE = "/data/telemetry.db"  # Ruta que luego mapearás a un volumen en Railway


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS metrics 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, device_id TEXT, val REAL)"""
    )
    conn.commit()
    conn.close()


init_db()


class Metric(BaseModel):
    device_id: str
    val: float


@app.post("/telemetry")
def save_metric(metric: Metric):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO metrics (device_id, val) VALUES (?, ?)",
        (metric.device_id, metric.val),
    )
    conn.commit()
    conn.close()
    return {"status": "ok"}


@app.get("/dashboard")
def get_metrics():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM metrics ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return {"latest": rows}