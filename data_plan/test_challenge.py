import pytest
from challenge import get_mb_available_next_month


def test_one_month_and_4mb_used():
    assert get_mb_available_next_month(10, 1, [4]) == 6


def test_two_months_and_12mb_used():
    assert get_mb_available_next_month(10, 2, [4, 12]) == 4


def test_three_months_and_1mb_used():
    assert get_mb_available_next_month(10, 3, [4, 12, 1]) == 13


def test_four_months_and_no_data_used():
    assert get_mb_available_next_month(10, 4, [4, 12, 1, 0]) == 23
