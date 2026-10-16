cars = ["Toyota", "Lexus", "Honda", "BMW"]

with open("cars.txt", "w") as file:
    for car in cars:
        file.write(car + "\n")

print("Car inventory saved successfully!")


with open("cars.txt", "r") as file:
    saved_cars = file.readlines()

print("Saved inventory:")

for car in saved_cars:
    print(car.strip())

