cars = ["Toyota", "Lexus", "Honda"]

def show_cars():
    print("Available cars:")

    for car in cars:
        print(car)

show_cars()


def add_car():
    new_car = input("Enter a car to add:")
    cars.append(new_car)
    print(new_car, "has been added!")

def count_cars():
    print("Total cars:", len(cars))

def search_car():
    car_name = input("Enter car to search:")

    if car_name in cars:
        print(car_name, "is available!")

    else:
        print(car_name, "is not available!")
    

while True:
    print("\nCAR DEALERSHIP MENU")
    print("1. View cars")
    print("2. Add a car")
    print("3. Exit")
    print("4. Count cars")
    print("5. Search for a car")

    choice = input("Choose an option:")

    if choice == "1":
        show_cars()

    elif choice == "2":
        add_car()

    elif choice == "3":
        print("Goodbye!")
        break
    elif choice == "4":
        count_cars()
    elif choice == "5":
        search_car()

    else:
        print("Invalid option. Try again.")

