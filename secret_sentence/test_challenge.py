import pytest
from challenge import get_decoded_sentence


def test_one_word():
    assert get_decoded_sentence("ipi") == "i"


def test_two_word():
    assert get_decoded_sentence("ipi lipikepe") == "i like"


def test_three_word():
    assert get_decoded_sentence("ipi lipikepe yopoupu") == "i like you"
