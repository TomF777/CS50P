from jar import Jar
import pytest

def test_init():
    jar_01 = Jar()

    # test default capacity value
    assert jar_01.capacity == 12

    # test default size value
    assert jar_01.size == 0
    del jar_01

    # test capacity only int
    with pytest.raises(ValueError):
        jar_02 = Jar(11.35)
        del jar_02


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    del jar


def test_deposit():
    # test adding allowed number of cookies
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    # test adding more cookies than jar’s capacity
    with pytest.raises(ValueError):
        jar.deposit(10)

    del jar


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7

    # test withdrawing allowed number of cookies
    jar.withdraw(6)
    assert jar.size == 1

    # test witdrawing more cookies than allowed
    with pytest.raises(ValueError):
        jar.withdraw(10)

    del jar
