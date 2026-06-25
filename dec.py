import sys
sys.path.append("project/hog")
from ucb import trace

def trace1(fn):
    """returns a value of fn
    fn - a function of 1 argument
    """
    def traced(x):
        print(f'calling {fn} on argument {x}')
        return fn(x)
    return traced

@trace1
def square(x):
    return x * x

@trace1
def sum_square_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total

