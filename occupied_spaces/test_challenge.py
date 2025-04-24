import pytest
from challenge import get_occupied_space_both_days


def test_one_space_empty_both_days():
    assert get_occupied_space_both_days(1, ".", ".") == 0


def test_one_space_occupied_both_days():
    assert get_occupied_space_both_days(1, "C", "C") == 1


def test_one_space_occupied_yesterday_not_today():
    assert get_occupied_space_both_days(1, "C", ".") == 0


def test_one_space_not_occupied_yesterday_but_today():
    assert get_occupied_space_both_days(1, ".", "C") == 0


def test_two_spaces_none_occupied_both_days():
    assert get_occupied_space_both_days(2, "..", "..") == 0


def test_two_spaces_both_occupied_both_days():
    assert get_occupied_space_both_days(2, "CC", "CC") == 2


def test_two_spaces_one_occupied_yesterday_both_today():
    assert get_occupied_space_both_days(2, "C.", "CC") == 1


def test_three_spaces_none_occupied_both_days():
    assert get_occupied_space_both_days(3, "...", "...") == 0


def test_three_spaces_all_occupied_yesterday_and_two_today():
    assert get_occupied_space_both_days(3, "CCC", "C.C") == 2


def test_three_spaces_all_occupied_both_days():
    assert get_occupied_space_both_days(3, "CCC", "CCC") == 3
