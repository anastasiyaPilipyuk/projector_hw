# Practice block 3
# Task 1 returns the second power.
def square(value: int) -> int:
    return value ** 2 if isinstance(value, int) else "Incorrect input data"


# Task 2 convert to Fahrenheit
def convert_cel_to_fahr(celsius_grade):
    if celsius_grade.isdigit():
        celsius_grade = float(celsius_grade)
        return (celsius_grade * 9 / 5) + 32


result = convert_cel_to_fahr(input("Enter value of temperature in Celsius: ").strip())
if result is not None:
    print(f"Temperature in Fahrenheit is {result}")
else:
    print("Incorrect input data")


# Task 3 swapping function
def do_swapping(string):
    swapped_str = ""
    for letter in string:
        if letter == str(letter).upper():
            swapped_str += str(letter).lower()
        else:
            swapped_str += str(letter).upper()
    return swapped_str


input_value = input("Enter string for do swapping: ")
print(f"'{do_swapping(input_value)}' is converted of '{input_value}'")


# Additional Task 1

# checking parameter on correct type
def check_correct_type(name, value, *arg):
    if not isinstance(value, arg):
        return f"Parameter '{name}' has wrong value. It has type {type(value)} instead of {arg} type"


# checking numerical parameters on is it int or float type
def check_all_number_params_type(*arg):
    param_names = "abc"
    i = 0
    for element in arg:
        result_ = check_correct_type(param_names[i], element, int, float)
        if result_ is not None:
            return result_
        else:
            if i == 0 and element == 0:
                return "Parameter a cannot be 0"
            else:
                i += 1


# checking all function parameters on correct types
def check_all_params_type(a, b, c, choose):
    result_of_checking_nums = check_all_number_params_type(a, b, c)
    if result_of_checking_nums is None:
        return check_correct_type("choose", choose, bool)
    else:
        return result_of_checking_nums


# searching roots with discriminant method
def discriminant(a, b, c):
    discriminant_value = b ** 2 - 4 * a * c
    if discriminant_value > 0:
        x1 = (-1 * b - discriminant_value ** 0.5) / (2 * a)
        x2 = (-1 * b + discriminant_value ** 0.5) / (2 * a)
        return f"The equation has two real roots: x1 = {round(x1, 2)}, x2= {round(x2, 2)}"
    elif discriminant_value == 0:
        x1 = -1 * b / (2 * a)
        return f"The equation has one real root: {round(x1, 2)}"
    else:
        return "The equation has two complex roots"


def resolve_equation(a, b, c, choose=True):
    result_of_checking = check_all_params_type(a, b, c, choose)
    if result_of_checking is None:
        if choose:
            return discriminant(a, b, c)
        else:
            pass
    else:
        return result_of_checking


result = resolve_equation(5, -8, 3, True)
print(result)
