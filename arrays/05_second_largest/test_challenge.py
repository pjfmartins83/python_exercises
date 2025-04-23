import pytest
from challenge import get_second_largest


def test_empty_array():
    assert get_second_largest([]) == None


def test_one_item():
    assert get_second_largest([5]) == None


def test_two_items():
    assert (get_second_largest([1, 2])) == 1


def test_more_than_two_items():
    assert (get_second_largest([1, 5, 7, 3, 6, 9, 2, 1, 7])) == 7


def test_equal_items():
    assert (get_second_largest([5, 5, 5, 5, 5])) == 5
