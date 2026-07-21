def square(x):
    return x * x

def odd(x):
    return x % 2 == 1

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest


def range_link(start, end):
    """Return a Link containing consecutive integers from start to end

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start <= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))


def map_link(f, s):
    """Return a Link that contains f(x) for each x in s
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only the element x of Link s for which f(x) is True
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest
    
def add(s, v):
    """Add v to an ordered list s with no repeats, returning modified s

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 6)
    Link(0, Link(1, Link(3, Lin(4, Link(5, Link(6))))))
    """
    assert s is not Link.empty
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s

def check_ordered(t, key=lambda x: x):
    """Check whether list s ordered from least to greatest.
    >>> t = Link(1, Link(3, Link(4)))
    >>> check_ordered(t)
    True
    >>> t = Link(1, Link(4, Link(3)))
    >>> check_ordered(t)
    False
    """
    if t is Link.empty or t.rest is Link.empty:
        return True
    elif key(t.first) > key(t.rest.first):
        return False
    else:
        return check_ordered(t.rest)
    
def merge(s, t):
    """Return a sorted link with the elements of sorted s & t.
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        return Link(s.first, merge(s.rest, t))
    else:
        return Link(t.first, merge(s, t.rest))
    
def merge_in_place(s, t):
    """Return a sorted Link with the elements from sorted s & t.
    >>> a = Link(1, Link(5))
    >>> b = Link(1, Link(4))
    >>> merge(a, b)
    Link(1, Link(1, Link(4, Link(5))))
    >>> a
    Link(1, Link(5))
    >>> b
    Link(1, Link(4))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    elif s.first <= t.first:
        s.rest = merge_in_place(s.rest, t)
        return s
    else:
        t.rest = merge_in_place(s, t.rest)
        return t