from fuel import convert, gauge
import pytest


def test_convert_half():
    assert convert("1/2") == 50


def test_convert_quarter():
    assert convert("1/4") == 25


def test_convert_full():
    assert convert("4/4") == 100


def test_convert_empty():
    assert convert("0/4") == 0


def test_convert_rounding():
    assert convert("1/3") == 33


def test_convert_invalid_letters():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("4/1")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")


def test_gauge_e():
    assert gauge(1) == "E"


def test_gauge_f():
    assert gauge(99) == "F"


def test_gauge_percent():
    assert gauge(50) == "50%"


def test_gauge_zero():
    assert gauge(0) == "E"


def test_gauge_hundred():
    assert gauge(100) == "F"
