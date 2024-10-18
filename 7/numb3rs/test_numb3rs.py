from numb3rs import validate

def test_validate1():
    assert validate("1.2.3.4") == True

def test_validate2():
    assert validate("1.2.3.1000") == False

def test_validate3():
    assert validate("cat") == False

def test_validate4():
    assert validate("1.2.3.4.5") == False