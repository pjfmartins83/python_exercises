import pytest
from challenge import get_drone_position


def test_no_imnput():
    assert get_drone_position("") == (0, 0)


def test_one():
    assert get_drone_position("UURRDDLL") == (0, 0)


def test_two():
    assert get_drone_position("UUUHRR") == (2, 3)


def test_three():
    assert get_drone_position("LLLLDD") == (-4, -2)
