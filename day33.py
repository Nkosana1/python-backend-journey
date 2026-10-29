import json

def save_inventory(cars):
    with open("inventory_day33.json", "w") as file:
        json.dump(cars, file, indent=4)

def load_inventory():
    try:
        with open("inventory_day33.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

cars = load_inventory()




def show_menu():
    print("\n=== CAR INVENTORY SYSTEM ===")
    print("1. View cars")
    print("2. Add car")
    print("3. Search car")
    print("4. Exit")
    print("5. Delete car")

while True:
    show_menu()

    choice = input("Choose an option (1-5):")

    if choice == "1":
        for car in cars:
            print(car["brand"], car["model"])
    elif choice == "2":
        brand = input("Enter car brand:")
        model = input("Enter car model:")

        new_car = {"brand": brand, "model": model}
        cars.append(new_car)
        save_inventory(cars)

        print("Car added successfully!")
    elif choice == "3":
        search = input("Search for a car:").strip().lower()
        found = False

        for car in cars:
            if search == car["brand"].lower() or search == car["model"].lower():
                print("Found:", car["brand"], car["model"])
                found = True

        if not found:
            print("Car not found!")

    elif choice == "5":
        brand = input("Enter car brand to delete:").strip().lower()
        found = False

        for car in cars:
            if car["brand"].lower() == brand:
                cars.remove(car)
                save_inventory(cars)
                print("Car deleted successfully!")
                found = True
                break

        if not found:
            print("Car not found!")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")