"""

The Challenge:

In basketball, three plays score points: a three-point shot, a two-point shot,
and a one-point free throw.
You just watched a basketball game between the Apples and Bananas and recorded
the number of successful three-point, two-point, and one-point plays for each
team. Indicate whether the game was won by the A, the game was won by
the B, or the game was a tie.

Input:

There are six lines of input.
The ﬁrst three give the scoring for the A,
and the latter three give the scoring for the B.

The ﬁrst line gives the number of successful three-point shots for the A.
The second line gives the number of successful two-point shots for the A.
The third line gives the number of successful one-point free throws for the A.
The fourth line gives the number of successful three-point shots for the B.
The fith line gives the number of successful two-point shots for the B.
The sixth line gives the number of successful one-point free throws for the B.

Output:

The output is a single character.
If the A scored more points than the B, output A (A for A).
If the B scored more points than the A, output B (B for B).
If the A and B scored the same number of points, T (T for Tie).

"""


def get_winner_team(a3, a2, a1, b3, b2, b1):
    apple_points = (a3 * 3) + (a2 * 2) + (a1 * 1)
    banana_points = (b3 * 3) + (b2 * 2) + (b1 * 1)
    if apple_points > banana_points:
        return "A"
    elif apple_points < banana_points:
        return "B"
    else:
        return "T"
