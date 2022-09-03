from plates import is_valid

def test_is_valid():
    assert is_valid('CS50') == True
def test_is_valid0():
    assert is_valid('hello, world') == False
def test_is_valid1():
    assert is_valid('cs50') == True
def test_is_valid2():
    assert is_valid('23') == False
def test_is_valid3():
    assert is_valid('cs') == True
def test_is_valid4():
    assert is_valid('cs.,32') == False
def test_is_valid5():
    assert is_valid('cs32') == True
def test_is_valid6():
    assert is_valid('cs05') == False
def test_is_valid7():
    assert is_valid('h') == False
