import pytest
from challenge import get_number_plays


def test_one():
    assert get_number_plays(1, 34, 0, 0) == 40


def test_two():
    assert get_number_plays(2, 0, 99, 0) == 80


def test_three():
    assert get_number_plays(3, 0, 0, 9) == 12
