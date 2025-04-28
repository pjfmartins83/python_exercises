import pytest
from challenge import get_cone_volume


def test_one():
    assert round(get_cone_volume(2, 3), 2) == 12.57


def test_two():
    assert round(get_cone_volume(3, 4), 2) == 37.70


def test_three():
    assert round(get_cone_volume(5, 10), 2) == 261.80
