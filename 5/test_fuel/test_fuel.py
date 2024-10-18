import fuel

def test_convert():
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/3") == 33
    assert fuel.convert("1/2") == 50
    assert fuel.convert("2/3") == 67
    assert fuel.convert("3/4") == 75
    assert fuel.convert("4/4") == 100

def test_gauge():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"