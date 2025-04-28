import pytest
from challenge import get_students_attendance


def test_one_student_absent_both_days():
    assert get_students_attendance(1, "A", "A") == 0


def test_one_student_present_only_one_day():
    assert get_students_attendance(1, "P", "A") == 0


def test_one_student_present_both_days():
    assert get_students_attendance(1, "P", "P") == 1


def test_two_students_present_both_days():
    assert get_students_attendance(2, "PP", "PP") == 2


def test_two_students_one_present_yesterday_another_one_present_today():
    assert get_students_attendance(2, "PA", "AP") == 0


def test_two_students_only_one_present_both_days():
    assert get_students_attendance(2, "PA", "PP") == 1


def test_three_students_two_absent_both_days_and_one_present_both_days():
    assert get_students_attendance(3, "AAP", "AAP") == 1


def test_three_students_two_present_both_days_and_one_absent_both_days():
    assert get_students_attendance(3, "PPA", "PPA") == 2


def test_three_students_all_present_both_days():
    assert get_students_attendance(3, "PPP", "PPP") == 3
