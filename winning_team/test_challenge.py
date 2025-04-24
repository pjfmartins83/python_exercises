import pytest
from challenge import get_winner_team


def test_apple_won():
    assert get_winner_team(10, 7, 5, 4, 6, 4) == "A"


def test_bananas_won():
    assert get_winner_team(5, 7, 5, 9, 9, 10) == "B"


def test_tie():
    assert get_winner_team(10, 7, 4, 10, 7, 4) == "T"
