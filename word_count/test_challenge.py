import pytest
from challenge import count_words


def test_one_word():
    assert count_words("teste") == 1


def test_two_words():
    assert count_words("Hello World") == 2


def test_three_words():
    assert count_words("Hello My Friend") == 3
