# Homework 1
# Practice Part 1
# Task_1
val1 = float(input("Enter first number: "))
val2 = float(input("Enter second number: "))
print("Numbers are:", val1, val2)

# Task_2
print(val1 + val2, val1 - val2, val1 * val2, val1 / val2, val1 // val2, val1 % val2, sep='\n')

# Task_3
# print("{} в {} степені це {}".format(val1, val2, val1 ** val2))
print(val1, "в", val2, "степені - це", val1 ** val2)

# Task_4 Unknown

# Task_5
name = input("Enter name: ")
surname = input("Enter surname: ")
age = input("Enter age: ")
print(name, surname, "You are", age, "years old")

# Practice Part 2
# Task_1

a = 32
b = 57
print("Old values a = {}, b = {}".format(a, b))

# first way
c = a
b = a
a = c
print("New values a = {}, b = {}".format(a, b))

# second way
a += b
b = a - b
a -= b
print("New values a = {}, b = {}".format(a, b))

# third way
a *= b
b = int(a / b)
a = int(a / b)
print("New values a = {}, b = {}".format(a, b))

# Task_2
arg1 = int(input("Enter first number: "))
arg2 = int(input("Enter second number: "))
print("Maximum is:", max(arg1, arg2))

# Task_3
value = int(input("Enter a number:"))
number_of_hundreds = value // 100
number_of_units = value % 10
reverse_value = number_of_units * 100 + number_of_hundreds + (value - number_of_hundreds * 100 - number_of_units)
print("Reversed number is", reverse_value)
