import pytest
from challenge import is_prime


def test_one():
    assert is_prime(0) == False


def test_two():
    assert is_prime(1) == False


def test_three():
    assert is_prime(2) == True


def test_four():
    assert is_prime(10) == False


def test_five():
    assert is_prime(7) == True


def test_six():
    assert is_prime(43) == True
