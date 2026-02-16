# Reverse a Number (No String)
num = 12345
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)

# armstrong num
num = 153
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit * digit * digit
    num //= 10

if sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")

# second largest
arr = [10, 20, 4, 45, 99]

largest = second = -999999

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)
