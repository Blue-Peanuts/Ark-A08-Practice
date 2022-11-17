from typing import List, Dict


def banish_disappointments(friends: Dict[str, List[bool]]):
    """Each keys of friends is a string reprenting the name of the friend.
    Each items of friends is a list of booleans representing if they pass a course or not.
    
    For example: if an item in friends has the value of Conrad: [False, False, True]
    it means that Conrad has passed 1 out of 3 courses
    
    This function should replace the values of the dictionary with 'Excellent', 'Mid', or 'Banished'
    depending on the performance of the friend.
    
    If the friend passes all of their courses, they get 'Excellent',
    else if they pass atleast 75% of their courses they get a 'Mid', else they get 'Banished'
    
    Example: [False, False, True, True] should be replaced by 'Banished' 
    
    >>> friends_1 = {'Conrad': [False, False, True, True],
    ...              'Josephine': [False, True, True, True],
    ...              'Sigmund': [True, True, True, True],
    ...              'Annie': [True, False, False, False]}
    >>> banish_disappointments(friends_1)
    >>> friends_1
    {'Conrad': 'Banished',\
 'Josephine': 'Mid',\
 'Sigmund': 'Excellent',\
 'Annie': 'Banished'}
    >>> friends_2 = {'Tiffany': [False, False, True, True, True],
    ...              'Shaul': [True, True, True, False],
    ...              'Kate': [True, True, True, False, False, True, True, True],
    ...              'Patrick': [True, True, True, True, True]}
    >>> banish_disappointments(friends_2)
    >>> friends_2
    {'Tiffany': 'Banished',\
 'Shaul': 'Mid',\
 'Kate': 'Mid',\
 'Patrick': 'Excellent'}
    """
    
    pass


def banish_after_electives(friends: Dict[str, List[bool]], electives_count: Dict[str, int]):
    """Dictionary friends contains the same data as the one in banish_disappointments().
    electives_count is a dictionary with names of the friend as keys, and the number of
    extra electives they will take as values.
    
    This function should act the same way as banish_disappointments(), but take into consider
    if the friend passes all the extra electives they are taking.
    
    For example, Conrad: [False, True, True] would normally be Banished, but
    if he takes two more electives, you should consider as if it was
    Conrad: [False, True, True, True, True], so he should be Mid instead

    >>> friends_1 = {'Conrad': [False, True, True],
    ...              'Josephine': [False, True, True, True],
    ...              'Sigmund': [True, True, True, True],
    ...              'Annie': [True, False, False, False]}
    >>> electives_count_1 = {'Conrad': 2,
    ...              'Josephine': 2,
    ...              'Sigmund': 2,
    ...              'Annie': 3}
    >>> banish_after_electives(friends_1, electives_count_1)
    >>> friends_1
    {'Conrad': 'Mid',\
 'Josephine': 'Mid',\
 'Sigmund': 'Excellent',\
 'Annie': 'Banished'}
    >>> friends_2 = {'Tiffany': [False, False, True, True, True, True],
    ...              'Shaul': [False, True, True, False],
    ...              'Kate': [False, False, True, True, True],
    ...              'Patrick': [True, True, True, True, True]}
    >>> electives_count_2 = {'Tiffany': 2,
    ...              'Kate': 10,
    ...              'Patrick': 1}
    >>> banish_after_electives(friends_2, electives_count_2)
    >>> friends_2
    {'Tiffany': 'Mid',\
 'Shaul': 'Banished',\
 'Kate': 'Mid',\
 'Patrick': 'Excellent'}
    """
    
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()