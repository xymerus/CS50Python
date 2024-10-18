from bank import value

def test_value():
    assert value("Hello") == "$0"
def test_value2():
    assert value("hello") == "$0"
def test_value3():
    assert value("HELLO") == "$0"
def test_value4():
    assert value("What's up, World?") == "$100"
def test_value5():
    assert value("hisdda") == "$20"