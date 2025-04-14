"""

The Challenge:

Count the frequency of each letter that appearance in a string.

"""


def frequency_counter(string):
    letters = {}
    for char in string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters
