temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")
# ternery operator
age = 22
# if age >= 18:
# message = "Eligible"
# else:
# message = "Not eligible"
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
# logical operators
high_income = False
good_credit = True
student = False
# and
# or
# not

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
# if high_income and good_credit:
 #   print("Eligible")
# else:
 #   print("Not eligible")

# short circuiting concept - if one condition found false it do not checks further it stops
# if found false in case of and operator
# true in case of or operator

# chaining comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible")

# quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

# for loops
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
# for number in range(1,4):
# for number in range(1, 10, 2):
# print("Attempt", number, number * ".")
for i in range(1, 6):
    print(i * "*")

for i in range(5, 0, -1):
    print(i * "*")

for i in range(1, 6):
    print((5-i) * " " + i * "*")

for i in range(1, 6):
    print((5 - i) * " " + (2*i - 1) * "*")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
        print()
successful = False
if successful: 
         print("Successful")
         break
else:
     print("Attempted 3 times and failed")

for x in range(5):
    for y in range(3):
        print(f"{x}, {y})")

# iterable
for x in range(5):

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
    print(f"We have {count} even numbers")

def greet(first_name, last_name):
# parameters inside def
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Mosh", "Hamedani")
greet("John", "Smith")
# arguments are the actual values given to the parameter
