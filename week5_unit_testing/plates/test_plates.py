from plates import is_valid


def test_correct_plate():
    assert is_valid("AAA222") == True
    assert is_valid("AA") == True

def test_incorrect_starts_with_one_number():
    assert is_valid("A5") == False

def test_incorrect_plate():
    assert is_valid("AAA22A") == False

def test_incorrect_length():
    assert is_valid("AAA3333") == False

def test_start_with_zero2():
    assert is_valid("BC0033") == False

def test_start_with_zero():
    assert is_valid("ABC!. ") == False

def test_start_with_numbers():
    assert is_valid("12AA88") == False
