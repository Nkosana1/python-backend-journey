from pydantic import BaseModel

import json
from fastapi import FastAPI

class Car(BaseModel):
    brand: str
    model: str

app = FastAPI()

def load_cars():
    with open("cars.json", "r") as file:
        return json.load(file)

@app.get("/")
def home():
    return {"message": "Welcome to my Car Inventory API"}


@app.get("/cars")
def get_cars():
    return load_cars()

@app.post("/cars")
def add_car(car:Car):
    return {
        "message": "Car received successfully!",
        "car": car   

    }







