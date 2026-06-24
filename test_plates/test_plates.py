from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True

def test_too_short():
    assert is_valid("A") == False

def test_too_long():
    assert is_valid("ABCDEFG") == False

def test_starts_with_number():
    assert is_valid("1ABC") == False

def test_second_char_number():
    assert is_valid("A1BC") == False

def test_starts_with_one_letter_only():
    assert is_valid("A1") == False

def test_starts_with_two_numbers():
    assert is_valid("12ABC") == False

def test_number_in_middle():
    assert is_valid("AAA22A") == False

def test_first_number_zero():
    assert is_valid("CS05") == False

def test_punctuation():
    assert is_valid("CS 50") == False

def test_valid_all_letters():
    assert is_valid("HELLO") == True

def test_valid_numbers_at_end():
    assert is_valid("AAA222") == True
