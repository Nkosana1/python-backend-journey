age = 39

print(age > 18)
print(age < 18)
print(age ==39)
print(age != 39)
print(age >= 39)
print(age <= 38)

age = int(input("Enter your age:"))

if age >= 18:
    print("You are an adult")
else:
    print("You are under 18")

age = int(input("Enter your age:"))

if age >= 18:
     print("Adult")
elif age >= 13:
     print("Teenager")
else:
     print("Child")