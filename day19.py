cars = [
    {"brand": "Toyota", "model": "Supra", "price": 4500000},
    {"brand": "Lexus", "model": "IS350", "price": 5200000},
    {"brand": "Honda", "model": "Civic", "price": 3000000},
    {"brand": "BMW", "model": "M3", "price": 7500000}

]

def search_car(brand):
    for car in cars:
        if car["brand"] .lower() == brand.lower():
            print("Found:", car["brand"], car["model"])
            return

    print(brand, "is not available")

search = input("Enter a car brand:")

search_car(search)