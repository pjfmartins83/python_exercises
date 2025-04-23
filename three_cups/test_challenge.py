import pytest
from challenge import get_ball_position


def test_no_swaps():
    assert get_ball_position("") == "left"


def test_one_swap_A():
    assert get_ball_position("A") == "middle"


def test_one_swap_B():
    assert get_ball_position("B") == "left"


def test_one_swap_C():
    assert get_ball_position("C") == "right"


def test_two_swaps_AB():
    assert get_ball_position("AB") == "right"


def test_two_swaps_AC():
    assert get_ball_position("AC") == "middle"


def test_two_swaps_BC():
    assert get_ball_position("BC") == "right"


def test_three_swaps_ABC():
    assert get_ball_position("ABC") == "left"
