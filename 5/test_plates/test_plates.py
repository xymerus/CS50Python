from plates import is_valid

def test_valid1():
    assert is_valid("CS50") == True
def test_valid2():
    assert is_valid("CS05") == False
def test_valid3():
    assert is_valid("CS50P") == False
def test_valid4():
    assert is_valid("PI3.14") == False