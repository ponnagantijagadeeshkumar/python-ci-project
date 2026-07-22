from calculator import *

def test_add():
    assert add(5, 5) == 10
    
def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(5, 5) == 25


def test_divide():
    assert divide(10, 2) == 5