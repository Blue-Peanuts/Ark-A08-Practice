from typing import List, Dict

def get_status(pass_list: List[bool]):
    """Each item of pass_list are booleans representing if they pass a course or not.
    For example: if the list has the value of: [False, False, True]
    it means that they passed 1 out of 3 courses
    
    Return 'Excellent', 'Mid', or 'Banished' depending on the performance on all courses.
    
    If they pass all of their courses, they get 'Excellent',
    else if they pass atleast 75% of their courses they get a 'Mid',
    else they get 'Banished'

    >>> get_status([False, True, True, False, True])
    'Banished'
    >>> get_status([False])
    'Banished'
    >>> get_status([True, True])
    'Excellent'
    >>> get_status([True, True, True, False])
    'Mid'
    >>> get_status([True, True, True, False, True, True])
    'Mid'
    """

    pass_percentage = pass_list.count(True) / len(pass_list) * 100    
    if pass_percentage >= 100:
        return 'Excellent'
    if pass_percentage >= 75:
        return 'Mid'
    return 'Banished'


def banish_disappointments(friends: Dict[str, List[bool]]):
    """Each keys of friends is a string reprenting the name of the friend.
    Each items of friends is a list of booleans representing if they pass a course or not.

    This function should replace the values of the dictionary with 'Excellent', 'Mid', or 'Banished'
    depending on the performance of the friend.

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
    
    for name in friends: 
        friends[name] = get_status(friends[name])


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
    for name in electives_count:
        # [item] * 3 means [item, item, item], which I find pretty useful here
        friends[name].extend([True] * electives_count[name])
    banish_disappointments(friends)


if __name__ == '__main__':
    import doctest
    doctest.testmod()