def smallest_indices(s):
    """Return the indices of all elements in a list s that have the smallest absolute value.
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> smallest_indices(s)
    [2, 4]
    """
    target = min(map(abs, s))
    return [index for index, value in enumerate(s) if abs(value) == target]

def largest_sum(s):
    """Assume len(s) > 1, return the largest sum of the two adjacent elements in the list s.
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> largest_sum(s)
    6
    """
    tmp = [s[index] + s[index+1] for index in range(len(s)-1)]
    return max(tmp)

def ends_with_same(s):
    """Return a dictionary mapping each digit d to the lists of elements in s that end with d.
    >>> s = [5, 8, 13, 21, 34, 55, 89]
    >>> ends_with_same(s)
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}

def has_equal(s):
    """Return the bool result of whether every element equal some other element in the list s
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> has_equal(s)
    False
    >>> s = [4, 3, 2, 3, 2, 4]
    >>> has_equal(s)
    True
    """
    return min([s.count(x) for x in s]) > 1

