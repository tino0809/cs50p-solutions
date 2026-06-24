from working import convert
import pytest


def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mixed():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"


def test_midnight():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_noon():
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")


def test_late_night():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"
