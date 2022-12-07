from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 10, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[3, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 1, 1, 1],
                [6, 2, 1, 4]]

FIVE_BY_FIVE = [[1, 2, 6, 5, 4],
                [9, 1, 1, 2, 9],
                [7, 1, 1, 1, 2],
                [9, 2, 1, 1, 7],
                [2, 6, 3, 9, 2]]


def puppies_killed(puppies_map: List[List[int]], cell: List[int]) -> int:
    """puppies_map represents a matrix full of puppies.
    The number in each cell represent the number of puppies
    in that cell.
    Return the number of puppies killed if you drop a bomb 
    which kills everything in a 3x3 radius on cell cell.

    >>> puppies_killed(THREE_BY_THREE, [1, 1])
    47
    >>> puppies_killed(FOUR_BY_FOUR, [0, 0])
    14
    >>> puppies_killed(FIVE_BY_FIVE, [1, 2])
    20
    """    
    total = 0;
    for row in puppies_map[max(0, cell[0] - 1): cell[0] + 2]:
        total += sum(row[max(0, cell[1] - 1): cell[1] + 2])
    return total
 ################### Alternative solution ##############################
 ## total = 0
 ## for i in range(cell[0] - 1, cell[0] + 2):
 ##     for j in range(cell[1] - 1, cell[1] + 2):
 ##         if is_valid_cell([i, j], len(puppies_map)):
 ##             total += puppies_map[i][j]
 ## return total


def least_puppies_killed(puppies_map: List[List[int]]) -> int:
    """You have a bomb and you have to drop it anywhere in puppies_map.
    The bomb would kill everything in a 3x3 radius.
    Given a map full of puppies, return the least
    amount puppies killed possible.
    
    Precondition: puppies_map is full of non_negative integers.
                  and the map is a square, (length = width).
    
    >>> least_puppies_killed(THREE_BY_THREE)
    17
    >>> least_puppies_killed(FOUR_BY_FOUR)
    7
    >>> least_puppies_killed(FIVE_BY_FIVE)
    11
    """

    least = puppies_killed(puppies_map, [0, 0])
    for i in range(len(puppies_map)):
        for j in range(len(puppies_map)):
            least = min(least, puppies_killed(puppies_map, [i, j]))
    return least


if __name__ == '__main__':
    import doctest
    doctest.testmod()