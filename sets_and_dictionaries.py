# Practice 1
from typing import NamedTuple

en_ua = {}
assert type(en_ua) == dict


class Translation(NamedTuple):
    en: str
    ua: str
    add_undef: bool


def add_color_translation(arr_translation: list, dictionary: dict) -> dict:
    for text_translation in arr_translation:
        if dictionary.get(text_translation.en) is None:
            if text_translation.add_undef:
                dictionary[text_translation.en] = "undefined"
            else:
                dictionary[text_translation.en] = text_translation.ua
    return dictionary


en_ua = add_color_translation([Translation(en="red", ua="червоний", add_undef=False),
                               Translation(en="green", ua="зелений", add_undef=False),
                               Translation(en="blue", ua=None, add_undef=True),
                               Translation(en="purple", ua=None, add_undef=True)], en_ua)


# Create a loop over existing values and print them to the console in the following format:
def print_dictionary(dictionary: dict):
    for item_en, item_ua in dictionary.items():
        print(f"{str(item_en).capitalize()} in Ukrainian is {str(item_ua)}")


print_dictionary(en_ua)


# Delete all key-values pairs from the dictionary if the lenght of value is lower than 5.
def del_short_values(dictionary: dict) -> dict:
    return {key: value for key, value in dictionary.items() if len(value) >= 5}


en_ua = add_color_translation([Translation(en="pink", ua="ро", add_undef=False),
                               Translation(en="grey", ua="сір", add_undef=False),
                               ], en_ua)


en_ua = del_short_values(en_ua)
print_dictionary(en_ua)

import random

capitals = {'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin', 'Italy': 'Rome',
            'USA': 'Washington', 'Canada': 'Ottawa', 'Switzerland': 'Bern', 'Austria': 'Vienna',
            'Belgium': 'Brussels', 'Sweden': 'Stockholm', 'Norway': 'Oslo', 'Denmark': 'Copenhagen',
            'Finland': 'Helsinki', 'Poland': 'Warsaw', 'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'}

command = ''
score = 0
count_of_lives = 3
random_key = random.choice(list(capitals.keys()))
hint = ""

while command != 'exit' and count_of_lives > 0:
    message = f"What is a capital of {random_key}? "
    if len(hint) > 0:
        message += f"This name starts with '{hint}' "
    message += "\n"
    command = input(message).strip().lower()
    # right answer
    if command == capitals[random_key].lower():
        score += 1
        print(f"RIGHT! +1 SCORE!")
        hint = ""
        random_key = random.choice(list(capitals.keys()))
    # wrong answer or exit
    else:
        if command != 'exit':
            count_of_lives -= 1
            hint = capitals[random_key][0:len(hint)+1]
            if count_of_lives > 0:
                print(f"Sorry, it's wrong answer. Try again or type 'exit'")
            else:
                print(f"Sorry, you loose the game")

    # print current score after each round
    print(f"Current score: {score}. Count of lives: {count_of_lives}\n")


# Optional
# Given a roman numeral, convert it to an integer.
def roman_to_int(s: str) -> int:
    dictionary_roman_arabic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dictionary_symbols_for_replace = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX",
                                      "XC": "LXXXX", "CD": "CCCC", "CM": "DCCCC"}

    for key, value in dictionary_symbols_for_replace.items():
        s = s.replace(key, value)

    result = 0
    for element in s:
        result += int(dictionary_roman_arabic[element])

    return result


def test_roman_to_int():
    result1 = roman_to_int("III")
    assert result1 == 3

    result1 = roman_to_int("LVIII")
    assert result1 == 58

    result1 = roman_to_int("MCMXCIV")
    assert result1 == 1994


test_roman_to_int()


# function that will do reverse operation - from integer to roman
def int_to_roman(s: int) -> str:
    dictionary_roman_arabic = {1: "I", 4: "IV", 5: "V", 9: "IX",
                               10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
                               400: "CD", 500: "D", 900: "CM", 1000: "M"}
    dictionary_roman_arabic = dict(sorted(dictionary_roman_arabic.items(), reverse=True))

    num_ = int(s)
    result = ""
    for key, value in dictionary_roman_arabic.items():
        while num_ >= int(key):
            result += value
            num_ -= key
    return result


def test_int_to_roman():
    result1 = int_to_roman(3)
    assert result1 == "III"

    result1 = int_to_roman(58)
    assert result1 == "LVIII"

    result1 = int_to_roman(1994)
    assert result1 == "MCMXCIV"


test_int_to_roman()


# determine if a number n is happy
def sum_of_sqr_digits(n: int):  # additional function that return the sum of the squares of the digits
    sum_ = 0
    for digit in str(n):
        sum_ += int(digit) ** 2
    return sum_


def is_happy(n: int) -> bool:
    if 1 <= n <= 230:
        sum_ = 0
        while sum_ != 1:
            sum_ = sum_of_sqr_digits(n)
            if sum_ == 1:
                return True
            elif sum_ == 4:
                return False
            else:
                n = sum_
    else:
        print(f"Incorrect number '{n}'. Value should be from 1 to 230")
        return False


def test_is_happy():
    result1 = is_happy(19)
    assert result1 is True

    result1 = is_happy(2)
    assert result1 is False


test_is_happy()


# Given a string s, find the length of the longest substring without repeating characters.
def length_of_longest_substring(s: str) -> int:
    max_length = 1
    current_str = s[0]
    i = 1
    while i < len(s) and current_str.find(s[i]) == -1:
        max_length += 1
        current_str += s[i]
        i += 1

    if len(s) > 1:
        max_length = max(length_of_longest_substring(s[1:]), max_length)
    return max_length


def test_length_of_longest_substring():
    result1 = length_of_longest_substring('abcabcabc')
    assert result1 == 3

    result2 = length_of_longest_substring('bbbbb')
    assert result2 == 1

    result3 = length_of_longest_substring("pwwkew")
    assert result3 == 3


test_length_of_longest_substring()

