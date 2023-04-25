# Task_1. Even or odd
number_for_test = input("Enter number: ").strip()
if number_for_test.isdigit():
    number_for_test = float(number_for_test)
    print("Number is even") if number_for_test % 2 == 0 else print("Number is odd")
else:
    print(f"Entered value {number_for_test} is not a number")

# Task_2. Return number between 0-9 in words
number_for_text = input("Enter number between [0; 9]: ").strip()
if number_for_text.isdigit():
    number_for_text = int(number_for_text)
    match number_for_text:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case 4:
            print("Four")
        case 5:
            print("Five")
        case 6:
            print("Six")
        case 7:
            print("Seven")
        case 8:
            print("Eight")
        case 9:
            print("Nine")
        case _:
            print("There is no text associated with such number")
else:
    print(f"Entered value {number_for_text} is not an integer number")

# Task 3 simple calc
number1 = input('Enter first number: ').strip()
number2 = input('Enter second number: ').strip()
math_operator = input('Enter operator: ').strip()

if number1.isdigit() and number2.isdigit():
    number1 = float(number1)
    number2 = float(number2)

    match math_operator:
        case '+':
            print(f"{number1} + {number2} = {number1 + number2}")
        case '-':
            print(f"{number1} - {number2} = {number1 - number2}")
        case '//':
            if number2 == 0:
                print('Floor division by zero is not allowed')
            else:
                print(f"{number1} // {number2} = {number1 // number2}")
        case '*':
            print(f"{number1} * {number2} = {number1 * number2}")
        case '/':
            if number2 == 0:
                print('Division by zero is not allowed')
            else:
                print(f"{number1} / {number2} = {number1 / number2}")
        case '**':
            print(f"{number1} ** {number2} = {number1 ** number2}")
        case _:
            print('Unknown operator')
else:
    print('Incorrect input data')

# Task 4 Initials for name and surname
name_str = input(" Enter your name: ").strip()
surname_str = input(" Enter your name: ").strip()

print(f"Your initials are: {name_str[0].upper()}.{surname_str[0].upper()}.")

# Practice section 2.
# Task 1 define season
month_input = input("**Input a month [01-12]:** ").strip()
if month_input.isdigit():
    month_input = int(month_input)
    if month_input == 12 or 1 <= month_input <= 2:
        print("It's a winter")
    elif 3 <= month_input <= 5:
        print("It's a spring")
    elif 6 <= month_input <= 8:
        print("It's a summer")
    elif 9 <= month_input <= 11:
        print("It's a fall")
    else:
        print("Incorrect month's number")
else:
    print("Incorrect input data")

# Task 2 next day
num_year = input("**Input a year:** ").strip()
num_month = input("**Input a month [1-12]:** ").strip()
num_day = input("**Input a day [1-31]:** ").strip()

if num_year.isdigit() and num_month.isdigit() and num_day.isdigit():
    num_day = int(num_day)
    num_month = int(num_month)
    num_year = int(num_year)
    if 1 <= num_day <= 31 and 1 <= num_month <= 12:
        if num_day == 31:
            num_day = 1
            if num_month == 12:
                num_month = 1
                num_year += 1
            else:
                num_month += 1
        else:
            num_day += 1
        print(f"The next date is [yyyy-mm-dd] {num_year}-{num_month}-{num_day}")
    else:
        print(f"Incorrect start date {num_year}-{num_month}-{num_day}")
else:
    print("Incorrect data")

# Task 3 compare length to 5
string_for_check = input("Input string for checking length: ")

if len(string_for_check) > 5:
    print(f"String '{string_for_check}' consist of more than 5 symbols")
elif len(string_for_check) == 5:
    print(f"String '{string_for_check}' consist of 5 symbols")
else:
    print(f"String '{string_for_check}' consist of less than 5 symbols")

# Task 4 Find all factors of number
positive_number = input("Enter number for searching factors: ").strip()
if positive_number.isdigit():
    positive_number = int(positive_number)
    i = 1
    while i <= positive_number:
        if positive_number % i == 0:
            print(f'{i} is a factor of number {positive_number}')
        i += 1
else:
    print("Incorrect input data")

# Task 5 check a triangle
side_1, side_2, side_3 = input("Enter triangle sides separated by coma: ").replace(' ', '').split(",")
if side_1.isdigit() and side_2.isdigit() and side_3.isdigit():
    side_1 = int(side_1)
    side_2 = int(side_2)
    side_3 = int(side_3)
    if side_1 == side_2 or side_1 == side_3 or side_2 == side_3:  # An isosceles triangle is a triangle
        # with (at least) two equal sides.
        print("This triangle is isosceles")
        if side_1 == side_2 == side_3:  # An equilateral triangle is a triangle in which all three sides are equal.
            print("This triangle is also equilateral")
    else:  # A scalene triangle is a triangle that has three unequal sides.
        print("This triangle is scalene")
else:
    print("Incorrect input data")

# Practice section 3.
# Task_1
for i in range(2, 11, 1):
    print(i)

# Task_2
i = 1
while i <= 10:
    print(i)
    i += 1

# Task_3 doubles number in a loop.
initial_number = input("Initial number: ").strip()
num_of_iteration = input("Number of iterations: ").strip()

if initial_number.isdigit() and num_of_iteration.isdigit():
    initial_number = int(initial_number)
    num_of_iteration = int(num_of_iteration)
    result = initial_number
    for i in range(num_of_iteration):
        result *= initial_number
        print(result)
else:
    print("Incorrect input data")

# Task_4 Fibonacci series
num_of_iteration = input("Number of iterations: ").strip()

if num_of_iteration.isdigit():
    num_of_iteration = int(num_of_iteration)

    first_number = second_number = third_number = 1
    result = "{}, {}".format(first_number, second_number)
    for i in range(3, num_of_iteration + 1, 1):
        first_number = second_number
        second_number = third_number
        third_number = first_number + second_number
        result += ", {}".format(third_number)
    print(f"Fibonacci series: {result}")
else:
    print("Incorrect input data")

# Task_5 Revert number
number = input("Enter number for reversing: ").strip()
if number.isdigit():
    number = int(number)
    revert_number = 0

    while number > 0:
        revert_number = revert_number * 10 + number % 10
        number = number // 10
    print(f"Revert number is {revert_number}")
else:
    print("Incorrect input data")

# Practice section 4
# Task_1 always asks to input
message_from_user = input("Input some command: ").lower()

while message_from_user != "q":
    message_from_user = input("Input some command: ").lower()

# Task_2 prints out the number if it is divisible by 3.
result_str = "Numbers that are divisible by 3: "
for i in range(101):
    if i % 3 == 0:
        result_str += "{}  ".format(i)
print(result_str)

# Task 3 iterate and print messages
number_for_loop = input("Input number for loop: ").strip()

if number_for_loop.isdigit():
    number_for_loop = int(number_for_loop)

    i = 1
    while i <= number_for_loop:
        if i % 3 == 0 and i % 5 == 0:
            print('foobar')
        elif i % 5 == 0:
            print('bar')
        elif i % 3 == 0:
            print('foo')
        i += 1
else:
    print('Incorrect input data')
