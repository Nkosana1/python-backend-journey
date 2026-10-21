import json

def load_inventory():
    try:
        with open("inventory_day26.json", "r") as file:
            cars = json.load(file)
        return cars

    except FileNotFoundError:
        return []

cars = load_inventory()

print("Inventory:", cars)
print("Total cars:", len(cars))