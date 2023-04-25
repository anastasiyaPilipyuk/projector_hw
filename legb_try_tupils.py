# Practice block 1
def outer_function(a, b):  # Create an outer function that will accept two parameters, a and b
    def inner_function():  # Create an inner function for calculate the addition of a and b
        return a + b

    return inner_function() + 5  # At last, an outer function will add 5 into addition and return it


# Practice block 2
# Tack 1
checked = False
while not checked:
    try:
        string_int = int(input("Input some int value: ").strip())
        message_for_quit = input("There is no errors in value. Enter Q to quit:").strip().lower()
        if message_for_quit == 'q':
            checked = True
        else:
            print('You should enter "Q/q" for quit')
    except ValueError:
        print('Please enter an integer')
        checked = False

# Task 2
try:
    string_ = input("Enter string value: ")
    index = int(input("Enter position of character: ").strip())
    if len(string_) < index:
        raise Exception(f"Entered index {index} more then length of string '{string_}'")
    else:
        print(f"Character as position {index} is '{string_[index - 1]}'")
except ValueError as e:
    print("Founded an error:", e)
except Exception as e:
    print("Founded an error:", e)

from random import randint


# Task 1
def dice_roll():
    return randint(1, 6)


# Task 2
counter_1, counter_2, counter_3, counter_4, counter_5, counter_6 = 0, 0, 0, 0, 0, 0
for i in range(10000):
    roll = dice_roll()
    match roll:
        case 1:
            counter_1 += 1
        case 2:
            counter_2 += 1
        case 3:
            counter_3 += 1
        case 4:
            counter_4 += 1
        case 5:
            counter_5 += 1
        case 6:
            counter_6 += 1

for i in range(1, 7):
    print(f"Count of rolls {i}", globals()[f"counter_{i}"])


# Task 3

def get_numeric_rating(value):
    try:
        float_value = float(value)
        if float_value < 0 or float_value > 100:
            raise ValueError
        return float_value
    except ValueError as e:
        return None


regions_count = input("Enter number of regions: ").strip()
result = ""
result_for_first = 0
COUNT_OF_VOTERS = 10000
PERCENTS_FOR_WIN = 50

if regions_count.isdigit():
    regions_count = int(regions_count)
    try:
        for i in range(1, regions_count + 1):
            rating = input(f"Enter rating for 1st candidate in {i}st region: ").strip()
            if get_numeric_rating(rating) is not None:
                rating = get_numeric_rating(rating)
                voters_first = int(COUNT_OF_VOTERS * rating / 100)
                result_for_first += voters_first
                result += f"Region {i}: {voters_first} votes for 1st candidate, {int(COUNT_OF_VOTERS - voters_first)}" \
                          f" votes for 2nd candidate\n"
            else:
                raise Exception(f"Rating '{rating}' has been entered incorrectly. "
                                f"It should be number in interval [0; 100]")

        result_percent = round(result_for_first * 100 / (COUNT_OF_VOTERS * regions_count), 2)
        if result_percent > PERCENTS_FOR_WIN:
            result += f"Result: 1nd candidate won with {result_for_first} votes and " \
                      f"{result_percent}% of all votes"
        else:
            result_percent = round((COUNT_OF_VOTERS * regions_count - result_for_first) * 100 /
                                   (COUNT_OF_VOTERS * regions_count), 2)
            result += f"Result: 2nd candidate won with {COUNT_OF_VOTERS * regions_count - result_for_first} " \
                      f"votes and {result_percent}%" \
                      f" of all votes"
        print(result)
    except Exception as e:
        print("Exception. ", e)
else:
    print("Incorrect number of regions")

# Practice section 4
tuple_full_name = ("Anastasiia", "Potopalska", 35)  # Create a tuple with your first name, last name, and age.
print(tuple_full_name[1])  # Print your last name using indexing.
name, surname, age = tuple_full_name[0], tuple_full_name[1], tuple_full_name[2]  # Create three variables
# in one line that extracted from tuple that you created in step 1.

for i in range(len(tuple_full_name[0])):  # Print your name letter by letter from this tuple
    print(tuple_full_name[0][i].upper())

new_tuple_full_name = tuple_full_name[0][1:], tuple_full_name[1][1:], tuple_full_name[2]  # Create a new tuple
# that contains all info from the first tuple but remove first letter from all strings
tuple_with_tuples = ((1, 2), (3, 4))


# Create a program that calculates the sum of all values in the tuple and print it to the console.
def sum_of_tuple_elements(tuple_value: tuple) -> float:
    sum_ = 0
    for k in range(len(tuple_value)):
        if str(tuple_value[k]).isdigit():
            sum_ += tuple_value[k]
        elif type(tuple_value[k]) == tuple:
            sum_ += sum_of_tuple_elements(tuple_value[k])
    return sum_


print(sum_of_tuple_elements((1, 2, (3, (69, 7)))))
