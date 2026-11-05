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
def add_car(car: Car):
    cars = load_cars()
    cars.append(car.model_dump())

    with open("cars.json", "w") as file:
        json.dump(cars, file, indent=4)

    return {
        "message": "Car received successfully!",
        "car": car   

    }







