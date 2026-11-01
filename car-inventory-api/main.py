from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my Car Inventory API"}

@app.get("/cars")
def get_cars():
    return [
        {"brand": "Toyota", "model": "Supra"},
        {"brand": "Porsche", "model": "911 GT3"}

    ]