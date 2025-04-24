"""

The Challenge:

You supervise a parking lot with n parking spaces.
- Yesterday, you recorded whether each parking space was
occupied by a car or was empty.
- Today, you again recorded whether each parking space was
occupied by a car or was empty.

Indicate the number of parking spaces that were occupied on both days.

The input consists of three parameters.

- The ﬁrst parameter contains integer n, the number of parking spaces.
- The second parameter contains a string of n characters for yesterday's
information, one character for each parking space.
- C indicates an occupied parking space (C for car),
- . indicates an empty parking space.
For example:

CC. means that the ﬁrst two parking spaces were occupied and the third was
empty.

- The third parameter contains a string of n characters for today's
information, in the same format as the second parameter.

Output

Output the number of parking spaces that were occupied on both days.

"""


def get_occupied_space_both_days(spaces, yesterday, today):
    count = 0
    for i in range(spaces):
        if yesterday[i] == today[i] == "C":
            count += 1
    return count
