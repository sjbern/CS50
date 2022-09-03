from um import count
def testWords():
    assert count('Hello, um, world') == 1

def testPeriods():
    assert count('This is, um... CS50') == 1
    assert count('Um... what are regular expressions?') == 1
    assert count('Humpty Dumpty dun did a fumpty') == 0

def testValid():
    assert count('um um um') == 3


