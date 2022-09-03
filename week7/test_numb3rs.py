from numb3rs import validate

def main():
    test_validate()
    test_validate2()

def test_validate():
    assert validate(r'255.255.255.255') == True
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1.') == False


def test_validate2():
    assert validate(r'512.512.512.512') == False
    assert validate('cat') == False
    assert validate(r'1000.1.1.1') == False
    assert validate(r'300.2.3.4') == False
    assert validate(r'1.300.3.4') == False
    assert validate(r'1.2.300.4') == False
    assert validate(r'1.2.3.300') == False




if __name__ == '__main__':
    main()