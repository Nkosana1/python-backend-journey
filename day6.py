age = int(input("Enter your age:"))
has_ticket = input("Do you have a ticket? yes/no:")

if age >= 18 and has_ticket == "yes":
   print("You may enter")
else:
   print("You may not enter")