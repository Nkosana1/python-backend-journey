import json

def load_inventory():
    with open("inventory_day29.json", "r") as file:
        return json.load(file)

def save_inventory(cars):
    with open("inventory_day29.json", "w") as file:
        json.dump(cars, file, indent=4)

cars = load_inventory()

print("Current inventory:", cars)

brand = input("Enter car brand:")
model = input("Enter car model:")

new_car = {"brand": brand, "model": model}

cars.append(new_car)

save_inventory(cars)

print("Car added successfully!")
print("Total cars:", len(cars))