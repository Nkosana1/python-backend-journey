new_car = input("Enter a new car:")

with open("car.txt", "a") as file:

print(new_car, "saved successfully!")

with open("cars.txt", "r") as file:
    print(file.read())