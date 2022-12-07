from typing import Dict, List

def count_item_occurence(lst: list) -> dict:
    """Return a dictionary that contains
    items in lst as keys, with values representing
    how many times the key appeared in lst.
    
    >>> count_item_occurence(['Red', 'Blue', 'Red', 'Blue', 'Blue', 'Purple']) == {
    ... 'Red': 2, 'Blue': 3, 'Purple': 1}
    True
    """
    dic = {}
    for item in lst:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    return dic


def value_of_shortest_key(dic: Dict[str, int]) -> str:
    """Return the value in dic that correspond to the
    shortest key in dic. 

    Precondition: no keys have the same length, and dic is not empty
    
    >>> value_of_shortest_key({'Green': 3, 'Blue': 2, 'Red': 1, 'Purple': 2})
    1
    """
    shortest_key = list(dic.keys())[0]
    ans = dic[shortest_key]
    
    for key in dic:
        if len(shortest_key) > len(key):
            shortest_key = key
            ans = dic[key]
    return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()