from math_functions import factorial

def test_factorial_positive():
    assert factorial(5) is 120

def test_factorial_zero():
    assert factorial(0) is 1

def test_factorial_negative():
    assert factorial(-5) is -1