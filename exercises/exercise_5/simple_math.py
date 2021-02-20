"""
A collection of simple math operations
"""

def simple_add(a,b):
    '''
    Returns the sum of two numbers a and b.
    
    Parameters
    ----------
    a, b : int or float
         The two numbers that are added together.
         
    Returns
    -------
    c : int or float
      The sum of a and b.
      
    Examples
    --------
    >>> simple_math.simple_add(1, 2)
    2
    >>> simple_math.simple_add(2, 3)
    5
    '''
    
    c = a + b
    return c

def simple_sub(a,b):
    '''
    Returns the difference between two numbers a and b by calculating c = a - b
    
    Parameters
    ----------
    a, b : int or float
         The two numbers used to calculate c.
         
    Returns
    -------
    c : int or float
      The difference between a and b.
      
    Examples
    --------
    >>> simple_math.simple_sub(1, 2)
    -1
    >>> simple_math.simple_sub(10, 5)
    5
    '''
    return a-b

def simple_mult(a,b):
    '''
    Returns the product of two numbers a and b by calculating c = a * b
    
    Parameters
    ----------
    a, b : int or float
         The two numbers used to calculate c.
         
    Returns
    -------
    c : int or float
      The product of a and b.
      
    Examples
    --------
    >>> simple_math.simple_mult(3, 2)
    6
    >>> simple_math.simple_mult(10, 5)
    50
    '''
    c = a * b
    return c

def simple_div(a,b):
    '''
    Returns the profraction of two numbers a and b by calculating c = a / b
    
    Parameters
    ----------
    a, b : int or float
         The two numbers used to calculate c.
         
    Returns
    -------
    c : float
      The fraction of a and b.
      
    Examples
    --------
    >>> simple_math.simple_div(3, 2)
    1.5
    >>> simple_math.simple_div(10, 2)
    5.0
    '''
    c = a / b
    return c

def poly_first(x, a0, a1):
    '''
    Returns the value of a first degree polynomial on the form 
    y = a0 + a1*x for a given a0, a1 and x.
    
    Parameters
    ----------
    x : int or float
      The x-value in a first degree polynomial on the form y = a0 + a1*x.
    a0 : int or float
       The a0-value in a first degree polynomial on the form y = a0 + a1*x.
    a1 : int or float
       The a1-value in a first degree polynomial on the form y = a0 + a1*x.

    Returns
    -------
    y : int or float
      The y-value in a first degree polynomial on the form y = a0 + a1*x.
      
    Examples
    --------
    >>> simple_math.poly_first(1, 2, 3)
    5
    >>> simple_math.poly_first(2, 3, 4)
    11
    '''
    y = a0 + a1*x
    return y

def poly_second(x, a0, a1, a2):
    '''
    Returns the value of a second degree polynomial on the form 
    y = a0 + a1*x + a2*x**2 for a given a0, a1, a2 and x.
    
    Parameters
    ----------
    x : int or float
      The x-value in a first degree polynomial on the form 
      y = a0 + a1*x + a2*x**2.
    a0 : int or float
       The a0-value in a first degree polynomial on the form 
       y = a0 + a1*x + a2*x**2.
    a1 : int or float
       The a1-value in a first degree polynomial on the form 
       y = a0 + a1*x + a2*x**2

    Returns
    -------
    y : int or float
      The y-value in a first degree polynomial on the form y = a0 + a1*x.
      
    Examples
    --------
    >>> simple_math.poly_first(1, 2, 3, 4)
    9
    >>> simple_math.poly_first(2, 3, 4, 5)
    31
    '''
    y = poly_first(x, a0, a1) + a2 * x**2
    return y
