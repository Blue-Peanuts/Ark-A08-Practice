from typing import List

def longest_string(lst: List[str]) -> str:
    """Return the string in list lst with the longest length.
    If the string is empty, return 0. If the length is tied,
    return the first occurence.

    >>> longest_string(['Conrad', 'Shaul', 'Christina'])
    'Christina'
    >>> longest_string(['Justin', 'Ark', 'Conrad'])
    'Justin'
    >>> longest_string([])
    0
    """
    pass


def delete_odd(lst: List[int]):
    """Modify list lst to have only even numbers.
    
    >>> lst = [0,1,2,3,4]
    >>> delete_odd(lst)
    >>> lst
    [0, 2, 4]
    """
    pass

def add_up_pair(lst: List[int]) -> List[int]:
    """Return a list that contains items that
    is created from adding up every two items
    in list lst.
    
    Precondition: len(lst) % 2 == 0
    
    >>> add_up_pair([1,5,2,5,2,1])
    [6, 7, 3]
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()