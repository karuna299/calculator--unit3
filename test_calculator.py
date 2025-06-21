from calculator import calculate

def test_addition():
    assert calculate(6, 5, "+") == 11

def test_multiplication():
    assert calculate(6, 5, "*") == 30

def test_division():
    assert calculate(6, 3, "/") == 2

def test_subtraction():
    assert calculate(6, 5, "-") == 1

def test_invalid_operator():
    assert calculate(6, 5, "%") == "invalid operator"