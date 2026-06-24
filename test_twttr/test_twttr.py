from twttr import shorten


def test_vowels_lowercase():
    assert shorten("hello") == "hll"


def test_vowels_uppercase():
    assert shorten("HELLO") == "HLL"


def test_mixed_case():
    assert shorten("Twitter") == "Twttr"


def test_no_vowels():
    assert shorten("gym") == "gym"


def test_numbers_and_punctuation():
    assert shorten("cs50!") == "cs50!"


def test_empty_string():
    assert shorten("") == ""
