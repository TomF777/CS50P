from seasons import spell_age_in_minutes
import pytest
from datetime import date



def test_valid_birthday_1():
    assert spell_age_in_minutes(date.fromisoformat("2011-09-12")) == "Seven million, eight hundred twelve thousand minutes"

def test_invalid_birthday_1():
    with pytest.raises(ValueError):
        spell_age_in_minutes(date.fromisoformat("12-23-12"))
