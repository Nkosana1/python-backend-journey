cars = ["Toyota","Lexus","Honda","BMW","Nissan"]

cars.append("Mercedes")

print(len(cars))


cars = ["Toyota", "Lexus", "Honda"]

for car in cars:
    print(car)

print("Total cars:", len(cars))

cars = ["Toyota","Lexus","Honda"]

count = 0

for car in cars:
    count = count + 1

print("Cars counted:", count)