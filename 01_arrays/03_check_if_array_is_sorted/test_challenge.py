import pytest
from challenge import is_sorted


def test_true():
    assert is_sorted([10, 20, 30, 40, 50]) == True


def test_false():
    assert is_sorted([20, 10, 50, 30, 40]) == False
