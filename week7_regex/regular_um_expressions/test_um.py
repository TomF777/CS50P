from um import count
import pytest

def test_valid_1():
    assert count("Um, thanks for the album.") == int(1)

def test_valid_2():
    assert count("um") == int(1)

def test_valid_3():
    assert count("um?") == int(1)

def test_valid_4():
    assert count("Um, thanks, um...") == int(2)

