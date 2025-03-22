import math_lib

def test_n_power():
    assert math_lib.n_power(2, 3) == 8
    assert math_lib.n_power(-2, 3) == -8
    assert math_lib.n_power(2, 0) == 1
    assert round(math_lib.n_power(2.5, 2), 5) == 6,25

def test_n_root():
    assert math_lib.n_root(27, 3) == 3
    assert math_lib.n_root(16, 2) == 4
    assert math_lib.n_root(2, 0) == 1
    assert round(math_lib.n_root(2, 2), 5) == 1,41421

def test_modulo():
    assert math_lib.modulo(10, 3) == 1
    assert math_lib.modulo(-10, 3) == 2
    assert math_lib.modulo(10, -3) == -2
    assert math_lib.modulo(-10, -3) == -1
    assert math_lib.modulo(10, 1) == 0
    assert math_lib.modulo(0, 5) == 0
    assert math_lib.modulo(7, 7) == 0
    assert math_lib.modulo(1000000000, 987654321) == 12345679
    assert math_lib.modulo(1, 2) == 1
    assert math_lib.modulo(-9876543210, 123456789) == 123456699
