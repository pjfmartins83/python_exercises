import pytest
from challenge import find_missing_number


def test_one():
    assert find_missing_number([1, 2, 3, 5, 6, 7, 8, 9]) == 4
