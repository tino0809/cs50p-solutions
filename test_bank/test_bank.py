from bank import value


def test_hello():
    assert value("hello") == 0


def test_hello_there():
    assert value("hello there") == 0


def test_hello_uppercase():
    assert value("HELLO") == 0


def test_h():
    assert value("howdy") == 20


def test_h_uppercase():
    assert value("Howdy") == 20


def test_other():
    assert value("what's up") == 100


def test_other_uppercase():
    assert value("WHAT'S UP") == 100
