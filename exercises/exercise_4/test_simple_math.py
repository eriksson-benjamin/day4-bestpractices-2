import simple_math
import numpy as np
import pytest

def test_simple_add():
    assert simple_math.simple_add(1, 2) == 3
    
def test_simple_sub():
    assert simple_math.simple_sub(10, 5) == 5
    assert simple_math.simple_sub(6.99, 5.99) == 1
    
def test_simple_mult():
    assert simple_math.simple_mult(7, 6) == 42    
    

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 10/3),
    (np.pi, np.e, np.pi/np.e),
    (6, 2, 3)
    ])
def test_simple_div(a, b, expected):
    assert simple_math.simple_div(a, b) == expected
    
@pytest.mark.parametrize('x, a0, a1, expected', [
    (14, 3, 2, 3 + 2*14),
    (121, 24, 34, 24 + 34*121)
    ])
def test_poly_first(x, a0, a1, expected):
    assert simple_math.poly_first(x, a0, a1) == expected
    

# Build a lot of tests for poly_second
a0 = np.random.sample(100)
a1 = np.random.sample(100)
a2 = np.random.sample(100)
x = np.random.sample(100)
expected = a0 + a1 * x + a2*x**2
    
list_of_tuples = [(X, A0, A1, A2, EXP) for X, A0, A1, A2, EXP in zip(x, a0, a1, a2, expected)]
    
@pytest.mark.parametrize('x, a0, a1, a2, expected', list_of_tuples)
def test_poly_second(x, a0, a1, a2, expected):
    assert simple_math.poly_second(x, a0, a1, a2) == expected
    
    
    
'''
def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

'''