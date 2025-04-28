import pytest
from challenge import get_sum


def test_one():
    assert get_sum([2, 7, 9, 11, 15], 9) == [[2, 7]]
