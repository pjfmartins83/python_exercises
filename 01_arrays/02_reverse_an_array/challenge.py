"""

Level: Beginner

Reverse an Array
Reverse the array in place.

input = [1, 2, 3, 4, 5]
output = [5, 4, 3, 2, 1]

"""


def reverse_an_array(input):
    left = 0
    right = len(input) - 1
    while left < right:
        input[left], input[right] = input[right], input[left]
        left += 1
        right -= 1
    return input
