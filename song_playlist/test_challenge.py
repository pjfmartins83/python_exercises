import pytest
from challenge import manage_playlist


def test_one():
    assert manage_playlist([(4, 1)]) == "A B C D E"


def test_two():
    assert manage_playlist([(1, 1), (4, 1)]) == "B C D E A"


def test_three():
    assert manage_playlist([(2, 1), (4, 1)]) == "E A B C D"


def test_four():
    assert manage_playlist([(3, 1), (4, 1)]) == "B A C D E"


def test_five():
    assert manage_playlist([(1, 1), (2, 1), (3, 1), (4, 1)]) == "B A C D E"


def test_six():
    assert manage_playlist([(1, 2), (2, 2), (3, 2), (4, 2)]) == "A B C D E"


def test_seven():
    assert manage_playlist([(1, 1), (4, 1), (2, 1), (3, 1)]) == "B C D E A"
