from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI()

@app.post("/check")
def prorate(req: Dict[str, Any]):
    old_price = float(req.get("old_price", 0))
    new_price = float(req.get("new_price", 0))
    days_remaining = float(req.get("days_remaining", 0))
    days_in_actual_month = float(req.get("days_in_actual_month", 30))
    spec = req.get("spec", "v1")

    diff = new_price - old_price

    if spec == "v1":
        charge = diff * (days_remaining / 30)
    else:
        charge = diff * (days_remaining / days_in_actual_month)

    return {"charge": charge}

@app.get("/")
def root():
    return {"status": "ok"}