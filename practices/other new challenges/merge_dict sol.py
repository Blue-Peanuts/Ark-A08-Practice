
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
    temp_dict = {}
    for key in dict_one:
        temp_dict[key] = dict_one[key]
    for key in dict_two:
        if key in temp_dict:
            temp_dict[key] = [dict_one[key], dict_two[key]]
            temp_dict[key].sort()
            temp_dict[key] = tuple(temp_dict[key])
        else:
            temp_dict[key] = dict_two[key]
    return temp_dict


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
    temp_dict = merge_dict_values(dict_one, dict_two)
    reversed_temp_dict = {}
    for key in temp_dict:
        if temp_dict[key] in reversed_temp_dict:
            val = reversed_temp_dict[temp_dict[key]]
            reversed_temp_dict[temp_dict[key]] = val + (key,)
        else:
            reversed_temp_dict[temp_dict[key]] = (key,)
    ans_dict = {}
    for key in reversed_temp_dict:
        if len(reversed_temp_dict[key]) > 1:
            temp = list(reversed_temp_dict[key])
            temp.sort()
            ans_dict[tuple(temp)] = key
        else:
            ans_dict[reversed_temp_dict[key][0]] = key
    return ans_dict



if __name__ == '__main__':
    import doctest
    doctest.testmod()