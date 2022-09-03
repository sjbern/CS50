from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
def test_upper():
    assert shorten("TWITTER") == 'TWTTR'
def test_mixed():
    assert shorten("TwItTeR") == 'TwtTR'
def test_num():
    assert shorten("1234") == '1234'
def test_sym():
    assert shorten("!?.,") == '!?.,'
