import pytest
from challenge import frequency_counter


def test_letter_frequency_counter_1():
    assert frequency_counter("a") == {"a": 1}


def test_letter_frequency_counter_2():
    assert frequency_counter("ab") == {"a": 1, "b": 1}


def test_letter_frequency_counter_3():
    assert frequency_counter("aab") == {"a": 2, "b": 1}


def test_letter_frequency_counter_4():
    assert frequency_counter("abcabcabc") == {"a": 3, "b": 3, "c": 3}
