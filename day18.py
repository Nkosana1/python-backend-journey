cars = [

     {
         "brand": "Toyota",
         "model": "Supra",
         "price": "4500000"
     },
     {
         "brand": "Lexus",
         "model": "IS350",
         "price": "5200000"

         
     },
     {
         "brand": "Honda",
         "model": "Civic",
         "price": "3000000"

         
     }

]

for car in cars:
    print(car["brand"], car["model"])



cars.append({
     
    "brand": "BMW",
    "model": "M3",
    "price": "7500000"

})
print("Total cars:", len(cars))


def search_car(brand):
    for car in cars:
        if car["brand"] == brand:
            print("Found:", car["brand"], car["model"])
            return

    print(brand, "is not available")

search_car("BMW")
search_car("Ferrari")


