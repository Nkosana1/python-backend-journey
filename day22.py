import json

car = {

    "brand": "Toyota",
    "model": "Supra",
    "year": 2022,
    "price": 4500000

}

with open("car_inventory.json", "w") as file:
    json.dump(car, file, indent=4)

print("Car inventory saved!")

with open("car_inventory.json", "r") as file:
    saved_car = json.load(file)

print("Brand:", saved_car["brand"])
print("Model:", saved_car["model"])
print("Price:", saved_car["price"])