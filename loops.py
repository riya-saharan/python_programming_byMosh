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
