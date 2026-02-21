# user defined functions
def addition(a, b):
    print(a+b)


addition(12, 45)


def addition1(a, b, c):
    return a+b+c


print(addition1(12, 45, 89))


def subtraction(q, w):
    return q-w


print(subtraction(12, 3))


def reverse(x):
    x = input("enter your string")
    y = x
    return y[::-1]


print(reverse('Riya'))
