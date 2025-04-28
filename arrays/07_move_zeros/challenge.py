"""

Level: Intermediate

Move Zeros to End
Rearrange the array so all 0s are at the end while maintaining the order of non-zero elements.

input = [1, 0, 0, 2, 3, 0, 4, 0, 5]
output = [1, 2, 3, 4, 5, 0, 0, 0, 0]

"""


def move_zeros(array):
    j = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[j] = array[i]
            j += 1

    for i in range(j, len(array)):
        array[i] = 0

    return array
