while True:
    try:

        price = int(input("Enter car price:"))
        print("Car price:", price)
        break

    except ValueError:
        print("Invalid price! Please try again.")

print("Price saved successfully!")