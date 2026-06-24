from datetime import date
from seasons import calculate_minutes


def test_one_regular_year():
    birth = date(2001, 1, 1)
    today = date(2002, 1, 1)
    assert calculate_minutes(birth, today) == 365 * 24 * 60


def test_one_leap_year():
    birth = date(2000, 1, 1)
    today = date(2001, 1, 1)
    assert calculate_minutes(birth, today) == 366 * 24 * 60


def test_two_years():
    birth = date(2001, 1, 1)
    today = date(2003, 1, 1)
    assert calculate_minutes(birth, today) == (365 + 365) * 24 * 60


def test_one_day():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 2)
    assert calculate_minutes(birth, today) == 1440


def test_same_day():
    birth = date(2000, 1, 1)
    today = date(2000, 1, 1)
    assert calculate_minutes(birth, today) == 0
