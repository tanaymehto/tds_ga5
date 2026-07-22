from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    old_price: float
    new_price: float
    days_remaining: int
    days_in_actual_month: int
    spec: str

@app.post("check")
def prorate(req: Request):
    diff = req.new_price - req.old_price

    if req.spec == "v1":
        charge = diff * (req.days_remaining / 30)
    elif req.spec == "v2":
        charge = diff * (req.days_remaining / req.days_in_actual_month)
    else:
        return {"error": "Invalid spec"}

    return {"charge": charge}