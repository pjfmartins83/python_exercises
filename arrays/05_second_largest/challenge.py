"""

Level: Beginner

Write a function to find the second largest element in an array.

input = [1, 5, 7, 3, 6, 9, 2, 1, 7]
output = 7


"""


def get_second_largest(input):
    if len(input) < 2:
        return None

    largest_number = float("-inf")
    second_largest_number = float("-inf")
    for item in input:
        if item > largest_number:
            second_largest_number = largest_number
            largest_number = item
        elif item > second_largest_number:
            second_largest_number = item
    return second_largest_number


print(get_second_largest([1, 5, 7, 3, 6, 9, 2, 1, 7]))
print(get_second_largest([1, 2]))
print(get_second_largest([5, 5, 5]))
