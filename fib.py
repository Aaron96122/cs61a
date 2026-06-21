# Here we calculate the fibnacci numbers in two manners
from math import sqrt
def fib1(n):
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr

def fib2(n):
    pred, curr = 1, 0
    k = 0
    while k < 5:
        pred, curr = curr, pred + curr
        k += 1
    return curr

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1 / guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

def improve_test():
    phi = 1/2 + sqrt(5)/2
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

def power(x, n):
    """Return x * x * x * ... * x for x repeated n times"""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n - 1)
    return find_zero(f, df)

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1

def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

if __name__ == "__main__":
    map_to_range(0,10, curried_pow(2))