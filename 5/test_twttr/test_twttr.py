from twttr import shorten

def test_twttr():
    assert shorten("twitter") == "twttr"

def test_twttr2():

    assert shorten("TWITTER") == "TWTTR"

def test_twttr3():
    assert shorten("Twitter") == "Twttr"

def test_twttr4():
    assert shorten("TwItTeR") == "TwtTR"