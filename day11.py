cars = ["Toyota","BMW","Mercedes","Honda"]
cars[1] = "Lexus"
cars.remove("Mercedes")

print(cars[0])
print(cars[2])

print(cars)

for car in cars:
    if car == "Lexus":
        print("Found Lexus!")
    else:
        print(car)

cars = ["Toyota","Lexus","Honda"]

if "BMW" in cars:
    print("BMW is available")
else:
    print("BMW is not available")



cars = ["Toyota","Lexus","Honda"]

choice = input("Enter a car:")

if choice in cars:
    print(choice, "is available")
else:
    print(choice,"is not available")