import pytest
from challenge import get_robo_position


def test_no_input():
    assert get_robo_position("") == 0


def test_one():
    assert get_robo_position("LRRLLS") == -1


def test_two():
    assert get_robo_position("RRRR") == 4


def test_three():
    assert get_robo_position("LLLSLL") == -5


def test_four():
    assert get_robo_position("SSSS") == 0
