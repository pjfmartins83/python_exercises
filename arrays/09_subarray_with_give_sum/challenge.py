"""

Level: Intermediate

Subarray with Given Sum:
Find a contiguous subarray that sums to a given value.

input 1 = [1, 2, 3, 7, 5]
input 2 (target) = 12

output = [2, 3, 7], [7, 5]

"""


def find_subarray(arr, target):
    result = []
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == target:
                result.append(arr[i : j + 1])
    return result
