"""

Level: Beginner

Write a function to find the largest and smallest elements in an array.

input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [9, 1]

"""


def get_max_and_min(input):
    max_value = float("-inf")
    min_value = float("inf")
    for num in input:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return [max_value, min_value]
