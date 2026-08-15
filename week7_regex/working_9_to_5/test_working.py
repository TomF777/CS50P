from working import convert
import pytest

def test_valid_time_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_valid_time_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_time_3():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_valid_time_4():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_valid_time_5():
    assert convert("11 AM to 9 PM") == "11:00 to 21:00"

def test_valid_time_6():
    assert convert("11:59 AM to 11:59 PM") == "11:59 to 23:59"

def test_valid_time7():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("11:30 PM to 1:15 AM") == "23:30 to 01:15"

def test_valid_time_8():
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"



def test_invalid_time_1():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_invalid_time_2():
    with pytest.raises(ValueError):
        convert("09:00 AM 17:00 PM")

def test_invalid_time_3():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

def test_invalid_time_4():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

def test_invalid_time_5():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_invalid_time_6():
    with pytest.raises(ValueError):
        convert("9 AM5 PM")

def test_invalid_time_7():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

def test_invalid_time_8():
    with pytest.raises(ValueError):
        convert("7:92 to 5:28")

def test_invalid_time_9():
    with pytest.raises(ValueError):
        convert("004:01 AM to 5 PM")
