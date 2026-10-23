import json

def save_inventory(cars):
    with open("inventory_28.json", "w") as file:
        json.dump(cars, file, indent=4)

    print("Inventory saved successfully!")

cars = [
    {"brand": "Toyota", "model": "Supra"},
    {"brand": "Honda", "model": "Civic"},
    {"brand": "BMW", "model": "M3"}
]
save_inventory(cars)

print("Total cars:", len(cars))