import pytest
from challenge import is_telemarketer


def test_telemarketer_ignore():
    assert is_telemarketer([8, 0, 0, 9]) == "ignore"
    assert is_telemarketer([9, 8, 8, 8]) == "ignore"
    assert is_telemarketer([8, 8, 8, 8]) == "ignore"
    assert is_telemarketer([9, 8, 8, 9]) == "ignore"


def test_telemarketer_answer():
    assert is_telemarketer([1, 2, 3, 4]) == "answer"
    assert is_telemarketer([7, 8, 8, 0]) == "answer"
    assert is_telemarketer([5, 6, 7, 8]) == "answer"
    assert is_telemarketer([9, 1, 1, 7]) == "answer"
