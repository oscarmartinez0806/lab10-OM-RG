import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
<<<<<<< HEAD
def sqaure_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)

=======

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
>>>>>>> 74a85a18bf429f8ff868e69aa5c92c54fdd3ed56
    if a == 0:
        raise ZeroDivisionError
    return a/b
def log(a,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b,a)
def exp(a,b):
    return a**b