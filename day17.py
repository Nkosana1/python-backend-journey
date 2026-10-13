car = {
    "brand": "Toyota",
    "model": "Supra",
    "price": "4500000"

}

print("Car:", car["brand"])
print("Model:", car["model"])

car["price"] = 4200000

print("Updated price:", car["price"])


car["color"] = "Red"

print("Car color:", car["color"])
print(car)


def show_car(car):
    print("Brand:", car["brand"])
    print("Model:", car["model"])
    print("Price:", car["price"])
    print("Color:", car["color"])

show_car(car)