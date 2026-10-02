number = 5

while number >= 1:
     print(number) 
     number = number - 1

number = int(input("Enter a starting number:"))

while number >= 1:
      print(number)
      number = number - 1

print("Finished!")


number = 1

while number <= 10:
    print(number)

    if number == 5:
        break
    number = number + 1

print("Loop finished!")




number = 0

while number < 5:
    number = number + 1

    if number == 3:
        continue

    print(number)



number = 0

while number < 5:
    number = number + 1

    if number == 2:
        continue

    if number == 4:
        break

    print(number)