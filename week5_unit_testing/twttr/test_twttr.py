from twttr import shorten
import sys

def test_no_vowels():
    assert shorten("qwrtpdgk") == "qwrtpdgk"
    assert shorten("ZXCVBNM") == "ZXCVBNM"


def test_with_vowels():
    assert shorten("asdfghjkl") == "sdfghjkl"


def test_with_numbers():
    assert shorten("1234") == "1234"


def test_capitalized_vowels():
    assert shorten("AEIOUz") == "z"


def test_punctuation():
    assert shorten(".,?") == ".,?"
