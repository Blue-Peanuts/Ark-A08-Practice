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
    # This is insertion sort
    # It brings the right most item to the left until it finds something smaller than it, then it stops.
    for i in range(len(lst) - 1): # i goes from 0 to N - 2
                                  # so this runs N - 1 times
        j = i + 1
        while j > 0 and lst[j] < lst[j - 1]: # j goes from i + 1 to 1, unless it finds a lower item
                                             # best case runs N times, if the list is already sorted (linear time complexity)
                                             # worst case it runs N - 1 + N - 2 + ... + 1 times (quadratic time complexity)
                                             # but if we look at comparisons, it runs 2 comparisons each loop, and needs one more comparison to end the loop
                                             # so worst case is N(N - 1)/2 + N comparisons (still quadratic)
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()