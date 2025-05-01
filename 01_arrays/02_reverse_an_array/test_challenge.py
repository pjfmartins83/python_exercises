import pytest
from challenge import reverse_an_array


def test_one():
    assert reverse_an_array([1, 2]) == [2, 1]


def test_two():
    assert reverse_an_array([-10, 0, 20, 5]) == [5, 20, 0, -10]


def test_three():
    assert reverse_an_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_four():
    assert reverse_an_array(["a", "b", "c"]) == ["c", "b", "a"]
