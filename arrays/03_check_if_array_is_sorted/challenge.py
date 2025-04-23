"""

Level: Beginner

Check if Array is Sorted
Determine if the array is sorted in ascending order.

input: [1, 2, 3, 4, 5]
output: true

input: [2, 1, 5, 3, 4]
output: false


"""


def is_sorted(input):
    for i in range(1, len(input)):
        if input[i] < input[i - 1]:
            return False
    return True
