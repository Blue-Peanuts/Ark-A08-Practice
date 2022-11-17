from typing import List


def create_group(people: list[str]) -> list[list[str]]:
    """Seperate people into groups, containing only people with the same
    first letter of the name, (e.g. Ark and Andy).
    
    The groups and name should be in alphabetical order. (use list.sort() function)
    
    >>> create_group(['Ark', 'Conrad', 'Christina', 'Patrick', 'Andy'])
    [['Andy', 'Ark'], ['Christina', 'Conrad'], ['Patrick']]
    """
    
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()