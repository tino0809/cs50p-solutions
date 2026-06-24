from um import count


def test_single():
    assert count("hello, um, world") == 1


def test_multiple():
    assert count("um, um, um") == 3


def test_case_insensitive():
    assert count("UM um Um") == 3


def test_not_substring():
    assert count("yummy") == 0


def test_not_substring_2():
    assert count("umbrella") == 0


def test_empty():
    assert count("") == 0


def test_no_um():
    assert count("hello world") == 0


def test_um_with_punctuation():
    assert count("um? um!") == 2
