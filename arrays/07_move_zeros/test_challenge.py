import pytest
from challenge import move_zeros


def test_one():
    assert move_zeros([1, 0, 0, 2, 3, 0, 4, 0, 5]) == [1, 2, 3, 4, 5, 0, 0, 0, 0]
