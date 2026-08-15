import bank


def test_start_with_hello():
    assert bank.value("hello") == 0

def test_start_with_hello_capitalized():
    assert bank.value("HELLO") == 0

def test_start_with_hello_phrase():
    assert bank.value("hello robson") == 0

def test_start_with_hello_phrase_capitalized():
    assert bank.value(" Hello robson ") == 0

def test_start_with_h_not_hello():
    assert bank.value("hopefully it works") == 20

def test_start_with_other_char():
    assert bank.value("qwertyui") == 100

def test_start_with_other_char_capitalized():
    assert bank.value(" ASDFGHJKL ") == 100
