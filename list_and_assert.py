# Practice block 1
# Task 1
def compute_difference(first: list, second: list) -> tuple:
    list_diff_first = [el for el in first if el not in second]
    list_diff_second = [el for el in second if el not in first]
    return list_diff_first, list_diff_second


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b'], ['e'])

    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])

    result3 = compute_difference([1, 2, 3], [4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 5, 6])

    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])

    test_compute_difference()


# Task 2
def sum_of_two(nums: list, target: int) -> list:
    for i in range(len(nums)):
        j = 0
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
            j += 1
    return "Condition is unreachable"


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 9)
    assert result1 == [0, 1]

    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]

    result3 = sum_of_two([3, 3], 6)
    assert result3 == [0, 1]

    result4 = sum_of_two([3, 8, 12], 6)
    assert result4 == "Condition is unreachable"


test_sum_of_two()


# Task 3
def longest_increasing_sequence(arr: list) -> int:
    result = (arr[0], 0)
    curr_element = arr[0]
    for i in range(len(arr)):
        j = i + 1
        count = 1
        if curr_element > arr[i] or i == 0:
            curr_element = arr[i]
            while j < len(arr):
                if curr_element < arr[j]:
                    count += 1
                    curr_element = arr[j]
                j += 1
            if result[1] < count:
                result = (arr[i], count)
            curr_element = arr[i]
    return result[1]


def test_sum_of_two():
    result1 = longest_increasing_sequence([9, 9, 4, 2])
    assert result1 == 1

    result2 = longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90])
    assert result2 == 7

    result3 = longest_increasing_sequence([4, 3, 5, 1, 6])
    assert result3 == 3


test_sum_of_two()

# Practice block 2
# Task 1
list_ = [1, 4, 2, 5]
sorted_list = sorted(list_)

assert list_ == [1, 4, 2, 5]
assert sorted_list == [1, 2, 4, 5]

# Task 2
population_list = [
    ('New York City', 8550405),
    ('Los Angeles', 3792621),
    ('Chicago', 2695598),
    ('Houston', 2100263),
    ('Philadelphia', 1526006),
    ('Phoenix', 1445632),
    ('San Antonio', 1327407),
    ('San Diego', 1307402),
    ('Dallas', 1197816),
    ('San Jose', 945942),
]

population_list.sort(key=lambda a: a[1])
total_count = sum([el[1] for el in population_list])
average_count = int(total_count / len(population_list))

assert total_count == 24889092
assert average_count == 2488909
