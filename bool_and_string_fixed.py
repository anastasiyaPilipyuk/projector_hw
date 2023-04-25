# Practice chapter 2
# Task_1
print("\"Print the text in which there will be a quote with double quotes.\"")
# Task_2
print("I'm Ukrainian")
# Task_3
print('''Print a line
that will be displayed 
on several lines
''')
# Task_4
print("Print text that doesn`t fit in \
one line but will be displayed \
in one line")


# Practice chapter 3
# Task_1
string_variable_1 = "Now is better"  # Create a variable with data type string.
length = len(string_variable_1)  # Count the length of this line.
# Task_2
string_variable_2 = "than never."  # Create another variable with string data type.
print(string_variable_1 + string_variable_2)  # Output the result of concatenation of these two variables.
# Task_3
print(string_variable_1, string_variable_2)  # Print the two previous variables, but with a space between them.

# Task_4 Get a string from user input. Check if the string is a palindrome.
string_for_checking = input("Enter line for check if is a palindrome: ")
message_for_print = str(string_for_checking == string_for_checking[::-1]).replace("True", "It is a palindrome").\
    replace("False", "It is not a palindrome")
print(message_for_print)

# Task_5 Replace age in the following string with your age.
original_string = "I'm 10 years old"
indexing_string = original_string[0: original_string.index("10")] + "35" + \
                  original_string[original_string.index("10")+2: len(original_string)]
replaced_string = original_string.replace("10", "35")   # replace function
print(f"Replace by indexing: {indexing_string}\nReplace by function: {replaced_string}")


# Practice chapter 4
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is %s and your age is %s years old" % (name, age))
print("Your name is {name} and your age is {age} years old".format(name=name, age=age))
print(f"Your name is {name} and your age is {age} years old")


# Practice chapter 5
string_1 = "Animals  "
string_2 = "  Badger"
string_3 = "honey bee"
string_4 = "   HoneyPot   "

# Task_1 str to lower
print(string_1.lower())
print(string_2.lower())
print(string_3.lower())
print(string_4.lower(), end="\n\n")

# Task_2 capitalize
print(string_1.upper())
print(string_2.upper())
print(string_3.upper())
print(string_4.upper(), end="\n\n")

# Task_3
# remove spaces from beginning
print(string_1.lstrip())
print(string_2.lstrip())
print(string_3.lstrip())
print(string_4.lstrip(), end="\n\n")

# remove spaces in the end of the line
print(string_1.rstrip())
print(string_2.rstrip())
print(string_3.rstrip())
print(string_4.rstrip(), end="\n\n")

# remove spaces on both sides of the line
print(string_1.strip())
print(string_2.strip())
print(string_3.strip())
print(string_4.strip(), end="\n\n")

# Task_4 Check the value if it's started with "be"
string_1 = "Bear"
string_2 = "bear"
string_3 = "BEAR"
string_4 = "bEar"

print(string_1.startswith("be"))
print(string_2.startswith("be"))
print(string_3.startswith("be"))
print(string_4.startswith("be"), "\n\n")

# Convert all rows for return True
string_1 = string_1.lower()
string_3 = string_3.lower()
string_4 = string_4.lower()

# Check again the value if it's started with "be"
print(string_1.startswith("be"))
print(string_2.startswith("be"))
print(string_3.startswith("be"))
print(string_4.startswith("be"))

# Task_5
input_str = "Somebody said something to Samantha."
# only for lowercase letter 's'
output_str = input_str.replace('s', 'x')
# and for uppercase letter 'S' if it's needed
# output_str = output_str.replace('S', 'x')
print(output_str)

# Task_6 Find letter in a line.
input_phrase = input("Enter phrase: ")
input_letter = input("Enter letter: ")
message_for_print = str(input_phrase.find(input_letter) >= 0).replace("True", "Yes!").replace("False", "No")
print(message_for_print)

# Task_7 Clean line
line = '12345!,_6--'
new_line = line.translate({ord('!'): None, ord(','): None,
                           ord('_'): None, ord('-'): None})
print(new_line)

# Task_8
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
fraction_in_percents = round((numerator / denominator) * 100, 2)
print(f'{fraction_in_percents}%')

# Task_9 Find a secret message
coding_string = 'X!xeXnxiXlX XtxeXrxcXeXsX Xax XsXXtXIX'
secret_string = coding_string.replace('x', '').replace('X', '')
secret_string = secret_string[::-1]
print(f'Secret message is "{secret_string}"')
