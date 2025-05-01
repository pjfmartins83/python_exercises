import pytest
from challenge import get_max_and_min


def test_one():
    assert get_max_and_min([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 1]


def test_two():
    assert get_max_and_min([-10, 0, 20, 5]) == [20, -10]


def test_three():
    assert get_max_and_min([42]) == [42, 42]


def test_four():
    assert get_max_and_min([-1, 2, -3]) == [2, -3]
