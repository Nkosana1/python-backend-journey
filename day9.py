while True:
    answer = input("Type quit to stop:")

    if answer == "quit":
        break

    print("You typed:",answer)

print("Program finished!")

while True:
    choice = input("Choose 1, 2, or quit:")

    if choice == "quit":
        break

    if choice == "1":
        print("You chose option 1")
    elif choice == "2":
        print("You chose option 2")
    else:
        print("Invalid choice")

print("Goodbye!")


while True:
    choice = input("Choose 1, 2, 3, or quit:")

    if choice == "quit":
        break

    if choice == "1":
        print("Check balance")
    elif choice == "2":
        print("Deposit")
    elif choice == "3":
        print("Withdraw")

    else:
        print("Invalid choice")

print("Goodbye!")