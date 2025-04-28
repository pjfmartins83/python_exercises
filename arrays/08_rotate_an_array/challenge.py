"""

Level: Intermediate

Rotate an Array:
Rotate the array to the right by k steps.

input 1 = [1, 2, 3, 4, 5, 6]
input 2 (k) = 2

output = [5, 6, 1, 2, 3, 4]

"""


def rotate_array(input, k):
    for i in range(k):
        input.insert(0, input.pop())
    return input
