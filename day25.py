try:
    with open("missing_cars.txt", "r") as file:
        cars = file.read()
        print(cars)

except FileNotFoundError:
    print("Inventory file not found!")

    with open("missing_cars.txt", "w") as file:
        file.write("Toyota\nHonda\nBMW")

    print("New inventory file created!")