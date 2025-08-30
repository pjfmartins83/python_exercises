import pytest
from challenge import is_palindrome


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Borror or Rob", True),
        ("Paulo", False),
        ("KayaK", True),
    ],
)
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected
