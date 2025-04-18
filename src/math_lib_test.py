import math_lib
import pytest

@pytest.mark.parametrize("a,b,expected", #test data for test_n_power()
[      
    (2,0,1),
    (2,3,8),
    (-2,3,-8),
])

def test_n_power(a,b,expected):
    assert math_lib.n_power(a,b) == expected

    assert round(math_lib.n_power(2.5, 2), 5) == 6.25

    with pytest.raises(ValueError, match="The exponent n must be a natural number, or 0"):
        math_lib.n_power(2, -1)
    with pytest.raises(ValueError, match="The exponent n must be a natural number, or 0"):
        math_lib.n_power(2, 1.5)

@pytest.mark.parametrize("a,b,expected", #test data for test_n_root()
[      
    (27,3,3),
    (-27,3,-3),
    (16,2,4),
])

def test_n_root(a,b,expected):
    assert math_lib.n_root(a,b) == expected

    assert round(math_lib.n_root(2, 2), 5) == 1.41421
    
    with pytest.raises(ValueError, match="The radical n must be a natural number"):
        math_lib.n_root(2, 0)
    with pytest.raises(ValueError, match="The radical n must be a natural number"):
        math_lib.n_root(2, -1)
    with pytest.raises(ValueError, match="The radical n must be a natural number"):
        math_lib.n_root(2, 1.5)

@pytest.mark.parametrize("a,b,expected",  #test data for test_modulo()
[
    (10,3,1),
    (-10,3,2),
    (10,-3,-2),
    (-10,-3,-1),
    (10,1,0),
    (0,5,0),
    (7,7,0),
    (1000000000,987654321,12345679),
    (1,2,1),
    (-9876543210,123456789,123456699),
])

def test_modulo(a,b,expected):
    assert math_lib.modulo(a, b) == expected
    with pytest.raises(ZeroDivisionError, match="Modulo by zero is not allowed"):
        math_lib.modulo(3, 0)

@pytest.mark.parametrize("a,b,expected",  #test data for test_addition()
[
    (2,3,5),
    (-2,-2,-4),
    (0,2,2),
    (0,-2,-2),
    (2,-2,0)
])
    
def test_addition(a,b,expected):
    assert math_lib.add(a,b)==expected

@pytest.mark.parametrize("a,b,expected",  #test data for test_substraction()
[
    (2,3,-1),
    (-2,2,-4),
    (0,2,-2),
    (0,-2,2),
    (2,-2,4)
])
    
def test_substraction(a,b,expected):
    assert math_lib.sub(a,b)==expected


@pytest.mark.parametrize("a,b,expected",  #test data for test_division()
[
    (2,2,1),
    (2,-2,-1),
    (-2,-2,1),
    (0,2,0),
    (0,-2,0),
    (5,2,2.5),
    (-5,2,-2.5),
    (200546,2,100273),
    (200546,-2,-100273)
])

def test_division(a,b,expected):
    assert math_lib.div(a,b)==expected
    with pytest.raises(ZeroDivisionError, match="Cannot divide with 0"):
        math_lib.div(2,0)


@pytest.mark.parametrize("a,b,expected",  #test data for test_multiplication()
[
    (2,2,4),
    (2,-2,-4),
    (-2,-2,4),
    (0,2,0),
    (0,-2,0),
    (5,0.5,2.5),
    (-5,0.5,-2.5),
])

def test_multiplication(a,b,expected):
    assert math_lib.mult(a,b)==expected
    

@pytest.mark.parametrize("a,expected",  #test data for test_factorial()
[
    (0,1),
    (5,120),
    (12,479001600),
])

def test_factorial(a,expected):
    assert math_lib.factorial(a)==expected
    with pytest.raises(ValueError, match="Only factorials of 0 and natural numbers"):
        math_lib.factorial(-1)
    with pytest.raises(ValueError, match="Only factorials of 0 and natural numbers"):
        math_lib.factorial(0.5)


@pytest.mark.parametrize("a,expected",  #test data for test_absolute_value()
[
    (0,0),
    (1,1),
    (-1,1),
])

def test_absolute_value(a,expected):
    assert math_lib.absolute(a)==expected
