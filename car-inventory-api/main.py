import json
from fastapi import FastAPI

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








