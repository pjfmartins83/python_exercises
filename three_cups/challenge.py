"""

The Challenge:

Borko has a row of three opaque cups: one at the left (location 1),
one at the middle (location 2), and one at the right (location 3).
There is a ball under the cup at the left.
It's our job to keep track of the location of the ball as Borko
swaps the locations of the cups.

Borko can make three types of swap:
A. Swap the left and middle cups
B. Swap the middle and right cups
C. Swap the left and right cups

For example, if Borko's ﬁrst swap is type A, then he
swaps the left and middle cups; because the ball starts at
the left, this swap moves it to the middle. If instead his ﬁrst
swap is type B, then he swaps the middle and right cups;
the left cup stays where it is, so the ball doesn't change
locations.

Input:
The input is one line of at most 50 characters. Each
character speciﬁes a type of swap that Borko makes: A, B, or C.

Output:
Output the ﬁnal location of the ball:
1 if the ball is at the left
2 if the ball is at the middle
3 if the ball is at the right

"""


def get_ball_position(swaps):
    ball_position = "left"
    for swap in swaps:
        if swap == "A":
            if ball_position == "left":
                ball_position = "middle"
            elif ball_position == "middle":
                ball_position = "left"
        elif swap == "B":
            if ball_position == "middle":
                ball_position = "right"
            elif ball_position == "right":
                ball_position = "middle"
        elif swap == "C":
            if ball_position == "left":
                ball_position = "right"
            elif ball_position == "right":
                ball_position = "left"
    return ball_position
