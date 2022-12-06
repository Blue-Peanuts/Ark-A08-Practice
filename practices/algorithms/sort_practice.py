def sort_ints(lst: list) -> None:
    """Sort lst, do not use list.sort().
    Practice insertion sort, selection sort, bubble sort.
    
    >>> lst = [1,6,132,4,2345,254,456,31,2,1]
    >>> sort_ints(lst)
    >>> lst
    [1, 1, 2, 4, 6, 31, 132, 254, 456, 2345]
    >>> lst = [1,6,-132,4,-254,456,31,2]
    >>> sort_ints(lst)
    >>> lst
    [-254, -132, 1, 2, 4, 6, 31, 456]
    >>> lst = []
    >>> sort_ints(lst)
    >>> lst
    []
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()