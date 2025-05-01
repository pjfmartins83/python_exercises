import pytest
from challenge import find_subarray


def test_one():
    assert find_subarray([1, 2, 3, 7, 5], 12) == [[2, 3, 7], [7, 5]]
