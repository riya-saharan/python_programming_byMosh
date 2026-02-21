sum = 0
num = 12345

while num > 0:
    rem = num % 10
    sum += rem
    num = num//10
print(sum)
