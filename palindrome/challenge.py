"""

A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.

The Challenge:

You need to create a function that will receive a string and return a boolean true for a palindrome and false is not a palindrome.

Input:
kayak

Output:
true

or

Input:
Borrow or rob

Output:
true

Input:
Paulo

Output:
false

"""


def is_palindrome(string):
    if not string:
        return False

    formatted_string = string.replace(" ", "").lower()
    reverse_string = ""

    for letter in formatted_string:
        reverse_string = letter + reverse_string

    return reverse_string == formatted_string
