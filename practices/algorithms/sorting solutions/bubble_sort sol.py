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
    # This is bubble sort.
    # It swaps the higher item to the right, until the rightmost index is the highest item.
    # After one inside loop the item at end index will be sorted.
    # It does this for each index.
    for end in range(len(lst) - 1, 0, -1): # end will start from N - 1 to 1
        for j in range(end): # this will run end times
                             # so this loop runs N - 1 + N - 2 + N - 3 + ... + 1 times
                             # means this algorithm has (n-1)(n)/2 comparisons
                             # and has quadratic time complexity            
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == '__main__':
    import doctest
    doctest.testmod()