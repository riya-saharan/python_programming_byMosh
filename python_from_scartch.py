print("Hello World")
print("*" * 10)
x = 3
# shift+ctrl+p for >
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"
print(students_count)
message = """
Hi Ankit,
I'm Riya Saharan from Sri Ganganagar
blah blah blahhh
"""
print(message)
course = "Python Pro"
print(len(course))
# if you want to access to a specific character in the string use square bracket notation
print(course[0])
# -1 gives last character
print(course[-1])
# if you want 3 characters
print(course[0:3])
print(course[0:])
print(course[:3])
# copy of the original string
print(course[:])
# backslash \ in python
# called excape character used to escape character after
coursee = "Python \"Programming"
# python "programming
print(coursee)
# backslash double quote \" is an escape sequence
coursee = 'Python \'Programming'
print(coursee)
coursee = "Python \\Programming"
print(coursee)
coursee = "Python\nProgramming"
print(coursee)
coursee = "Python\tProgramming"
print(coursee)
first = "Mosh"
last = "Hamedani"
# full = first + " " + last
# print(full)
full = f"{first} {last}"
print(full)
# full = f"{len(first)} {2 + 2}
# 4 4
# everything in python is an object and objects have functions we call methods that we can access using the dot notation
# course.
# here course is an object and we use dot notation to access its functions or methods
# upper() to convert a string to uppercase
course = "  python programming"
print(course.upper())
# all capt
print(course.lower())
print(course.title())
print(course.strip())
# lstrip and rstrip
# index of character or string
print(course.find("pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)
# these all were methods
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
# this generates floating no 3.333333... use double slash to get 3
print(10 // 3)
print(10 % 3)
print(10 ** 3)
# augmented assignment operator
x = 10
x = x + 3
x += 3
