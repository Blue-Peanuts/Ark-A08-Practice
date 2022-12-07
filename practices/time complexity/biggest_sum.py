from typing import List


# Try to guess what the best case and worst case time complexity is for this function.
# Also guess the number of comparisons
# Then check your answer with the answer file in the same folder I provided.

def biggest_sum(lst: List[int]) -> int:
    """Return the biggest sum of two integers in lst.
    
    Precondition: len(lst) >= 2
    
    >>> biggest_sum([1,2,2,2,4,6,7])
    13
    >>> biggest_sum([1,8,2,-20,4,6,7])
    15
    >>> biggest_sum([10, -100])
    -90
    """
    big = lst[0] + lst[1]
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] + lst[j] > big:
                big = lst[i] + lst[j]
    return big


if __name__ == '__main__':
    import doctest
    doctest.testmod()