from pydantic import BaseModel

import json
from fastapi import FastAPI, HTTPException

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

@app.post("/cars", status_code=201)
def add_car(car: Car):
    cars = load_cars()

    for existing_car in cars:
        if (
 
            existing_car["brand"].strip().lower() == car.brand.strip().lower()
            and existing_car["model"].strip().lower() == car.model.strip().lower()

        ):

            raise HTTPException(
                status_code=409,
                detail="This car already exists!"

            )
    cars.append(car.model_dump())

    with open("cars.json", "w") as file:
        json.dump(cars, file, indent=4)

    return {
        "message": "Car saved successfully!",
        "car": car   

    }


@app.delete("/cars/{brand}/{model}", status_code=200)
def delete_car(brand:str,model:str):
    cars = load_cars()

    for car in cars:
        if (
            car["brand"].strip().lower() == brand.strip().lower()
            and car["model"].strip().lower() == model.strip().lower()
        ):
            cars.remove(car)

            with open("cars.json", "w") as file:
                json.dump(cars, file, indent=4)

            return {"message": "Car deleted successfully!"}


    raise HTTPException(
        status_code=404,
        detail="Car not found!"

    )




