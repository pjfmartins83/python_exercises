"""

The Challenge:

- Martha goes to a casino and brings n quarters.
- The casino has three slot machines, and she plays them in order until she has
no quarters left.
That is:
- First slot machine, then the second, then the third,
then back to the ﬁrst, then the second, and so on.
- Each play costs one quarter.
- The slot machines operate according to the following rules:
    - The ﬁrst slot machine pays 30 quarters every 35th time it is played.
    - The second slot machine pays 60 quarters every 100th time it is played.
    - The third slot machine pays 9 quarters every 10th time it is played.
    - No other plays pay anything.

Determine the number of times Martha plays before she has no quarters left.

Input

The input consists of four parameters.

- The ﬁrst parameter contains an integer n, the number of quarters that Martha
brings to the casino.
- The second parameter contains an integer indicating the number of times
that the ﬁrst slot machine has been played since it last paid.
obs: These plays occurred prior to Martha arriving, and Martha’s plays continue
from there.

For example:
Suppose that the ﬁrst slot machine has been played 34 times since it last paid.
Then, Martha will win 30 quarters the ﬁrst time she plays it.

- The third parameter contains an integer indicating the number of times that
the second slot machine has been played since it last paid.
- The fourth parameter contains an integer indicating the number of times that
the third slot machine has been played since it last paid.

Output

Output the following sentence, where x is the number of times Martha plays
before she has no quarters left:

Martha plays x times before going broke.

"""


def get_number_plays(quarters, machine1_plays, machine2_plays, machine3_plays):
    number_of_plays = 0

    while quarters > 0:

        # machine1
        quarters -= 1
        number_of_plays += 1
        machine1_plays += 1
        if machine1_plays == 35:
            quarters += 30
            machine1_plays = 0
        if quarters == 0:
            break

        # machine2
        quarters -= 1
        number_of_plays += 1
        machine2_plays += 1
        if machine2_plays == 100:
            quarters += 60
            machine2_plays = 0
        if quarters == 0:
            break

        # machine3
        quarters -= 1
        number_of_plays += 1
        machine3_plays += 1
        if machine3_plays == 10:
            quarters += 9
            machine3_plays = 0
        if quarters == 0:
            break

    return number_of_plays
