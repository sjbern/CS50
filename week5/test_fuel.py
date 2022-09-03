from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('1/2') == 50

def test_convert2():
    assert convert('99/100') == 99

def test_gauge():
    assert gauge(50) == '50%'

def test_gauge2():
    assert gauge(99) == 'F'

def test_gauge3():
    assert gauge(1) == 'E'

def test_zde():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_ve():
    with pytest.raises(ValueError):
        convert('cat/dog')