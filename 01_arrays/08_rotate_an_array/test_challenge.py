import pytest
from challenge import rotate_array


def test_one():
    assert rotate_array([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
