
def merge_dict_values(dict_one: dict, dict_two: dict) -> dict:
    """Return a new dictionary by merging dict_one and dict_two

    If the dictionaries have the same keys, put the values in a tuple.
    
    sort the values in all the tuples
    
    Assume all keys and values are immutable

    >>> merge_dict_values({1: 'a', 2: 'b'}, {1: 'c'}) == {1: ('a', 'c'), 2: 'b'}
    True
    >>> merge_dict_values({1: 'a', 2: 'b'}, {1: 'b', 2: 'a'}) == {1: ('a', 'b'), 2: ('a', 'b')}
    True
    >>> merge_dict_values({1: 'a', 2: 'b'}, {1: 'b', 2: 'a', 3: 'c'}) == {1: ('a', 'b'), 2: ('a', 'b'), 3: 'c'}
    True
    """
    pass


def merge_dict_values_and_keys(dict_one: dict, dict_two: dict) -> dict:
    """Return a new dictionary by merging dict_one and dict_two

    If the dictionaries have the same keys, put the values in a tuple.
    If multiple keys have the same values, combine the keys into a tuple
    
    sort the values in all the tuples
    
    Assume all keys and values are immutable
    
    >>> merge_dict_values_and_keys({1: 'a', 2: 'b'}, {1: 'c'}) == {1: ('a', 'c'), 2: 'b'}
    True
    >>> merge_dict_values_and_keys({1: 'a', 2: 'b'}, {1: 'b', 2: 'a', 3: 'c'}) == {(1, 2): ('a', 'b'), 3: 'c'}
    True
    >>> merge_dict_values_and_keys({1: 'a', 2: 'b'}, {1: 'b', 2: 'a', 3: 'c'}) == {(1, 2): ('a', 'b'), 3: 'c'}
    True
    >>> merge_dict_values_and_keys({1: 'a', 4: 'b'}, {4: 'b', 2: 'a', 3: 'a'}) == {(1, 2, 3): 'a', 4: ('b', 'b')}
    True
    >>> merge_dict_values_and_keys({2: 'a', 1: 'a', 3: 'a'}, {1: 'b', 2: 'b', 3: 'b'}) == {(1, 2, 3): ('a', 'b')}
    True
    """
    pass



if __name__ == '__main__':
    import doctest
    doctest.testmod()