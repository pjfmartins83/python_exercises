"""

Level: Beginner

Write a function that receives an array and returns another array without duplicates.

Input: [1, 2, 3, 3, 4, 5, 3]
Output: [1, 2, 3, 4, 5]


"""


def remove_duplicates(arr):
    uniques = []
    for item in arr:
        if item not in uniques:
            uniques.append(item)
    return uniques
