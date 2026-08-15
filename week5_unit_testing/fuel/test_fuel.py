from fuel import gauge, convert
import pytest

def test_convert_correct_values():
    assert convert("5/10") == 50
    assert convert("1/100") == 1
    assert convert("1/101") == 1

def test_convert_x_y_not_int():
    with pytest.raises(ValueError):
        convert("12.5/80")

    with pytest.raises(ValueError):
        convert("20/90.2")

def test_convert_x_y_negative():
    with pytest.raises(ValueError):
        convert("-20/100")

    with pytest.raises(ValueError):
        convert("10/-30")

def test_convert_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("30/0")


def test_gauge_empty():
    assert gauge(1) == "E"


def test_gauge_normal_values():
    assert gauge(20) == "20%"


def test_gauge_full():
    assert gauge(99) == "F"

