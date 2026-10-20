import json

try:
    with open("inventory_day26.json", "r") as file:
        cars = json.load(file)

    print("Inventory loaded:", cars)

except FileNotFoundError:
    print("Inventory file missing!")

    cars = [
        {"brand": "Toyota", "model": "Supra"},
        {"brand": "Honda", "model": "Civic"}

    ]

    with open("inventory_day26.json", "w") as file:
        json.dump(cars, file, indent=4)

    print("New JSON inventory created!")

except json.JSONDecodeError:
    print("Inventory contains invalid JSON!")
    print("Please check the file.")
