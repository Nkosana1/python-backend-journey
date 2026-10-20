import json

with open("car_inventory.json", "r") as file:
    car = json.load(file)

print("Original price:", car["price"])

car["price"] = 4000000

with open("car_inventory.json", "w") as file:
    json.dump(car, file, indent=4)

print("Updated price:", car["price"])