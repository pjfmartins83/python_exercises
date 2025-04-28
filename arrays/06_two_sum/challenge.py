"""

Level: Intermediate

Two Sum Problem:
Find two numbers in an array that add up to a specific target.

Input 1 = [2, 7, 9, 11, 15]
Input 2 (target) = 9

Output = [2, 7]

"""


def get_sum(input, target):
    result = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i] + input[j] == target:
                result.append([input[i], input[j]])
    return result
