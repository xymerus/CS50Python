from working import convert

def test1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"