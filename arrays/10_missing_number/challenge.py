"""

Level: Intermediate

Find Missing Number
In an array of n integers from 1 to n+1, find the missing number.

input = [1, 2, 3, 5, 6, 7, 8, 9]
output = 4

"""

# Fórmula da Soma Esperada: ((n + 1) * (n + 2)) / 2


def find_missing_number(arr):
    n = len(arr)
    expected_sum = (n + 1) * (n + 2) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


print(find_missing_number([1, 2, 3, 5, 6, 7, 8, 9]))
