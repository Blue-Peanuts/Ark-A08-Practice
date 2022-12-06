def sort_ints(lst: list) -> None:
    """Sort lst, do not use list.sort().
    Practice insertion sort, selection sort, bubble sort.
    
    >>> lst = [1, 6, 132, 4, 2345, 254, 456, 31, 2, -1]
    >>> sort_ints(lst)
    >>> lst
    [-1, 1, 2, 4, 6, 31, 132, 254, 456, 2345]
    >>> lst = [1, 6, -132, 4, -254, 456, 31, 2]
    >>> sort_ints(lst)
    >>> lst
    [-254, -132, 1, 2, 4, 6, 31, 456]
    >>> lst = []
    >>> sort_ints(lst)
    >>> lst
    []
    >>> lst = [1, 6, -132, 4, -254, 456, 31, 20000]
    >>> sort_ints(lst)
    >>> lst
    [-254, -132, 1, 4, 6, 31, 456, 20000]
    """
    # This is selection sort.
    # It looks through the list for the lowest number and swap it with the position it should be in
    for i in range(len(lst) - 1): # Runs N - 1 times, take the form of 1 to N - 2
        min_num_index = i
        for j in range(i + 1, len(lst)): # runs N - i - 1 times
                                         # i can be from 0 to N - 1
                                         # so this loop runs N - 1 + N - 2 + N - 3 + ... + 1 times
                                         # means this algorithm has (n-1)(n)/2 comparisons
                                         # and has quadratic time complexity
            if lst[min_num_index] > lst[j]:
                min_num_index = j
        lst[i], lst[min_num_index] = lst[min_num_index], lst[i]


if __name__ == '__main__':
    import doctest
    doctest.testmod()