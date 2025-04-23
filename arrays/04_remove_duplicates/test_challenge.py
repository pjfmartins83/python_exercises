import pytest
from challenge import remove_duplicates


def test_one():
    assert remove_duplicates([1, 2, 3, 3, 4, 5, 3]) == [1, 2, 3, 4, 5]


def test_two():
    assert remove_duplicates([1, 1, 2, 2, 1, 1, 2, 2]) == [1, 2]
