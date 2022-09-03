from bank import value

def test_lose():
    assert value('hello') == 0
    assert value('Hello') == 0
    assert value('hello dude') == 0

def test_med():
    assert value('hi') == 20
    assert value('Hola') == 20
    assert value('HEYO') == 20

def test_win():
    assert value('lala') == 100
    assert value('wtf!!!') == 100
    assert value('what in the hell are you doing here?') == 100