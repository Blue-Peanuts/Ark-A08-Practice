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

# Try to guess what the best case and worst case time complexity is for this function.
# Also guess the number of comparisons
# Then check your answer with the answer file in the same folder I provided.
# Let N be the length/width of the table in this case

def valid_2x2(table: List[List[int]], wanted_sum: int) -> bool:
    """Check if there is a 2x2 square in table that sums to wanted_sum
    The table is a square (length = width)

    >>> valid_2x2(THREE_BY_THREE, 5)
    False
    >>> valid_2x2(FOUR_BY_FOUR, 10)
    True
    >>> valid_2x2(FIVE_BY_FIVE, 5)
    True
    >>> valid_2x2(FIVE_BY_FIVE, 19)
    True
    >>> valid_2x2(FIVE_BY_FIVE, 13)
    True
    >>> valid_2x2(FIVE_BY_FIVE, 130)
    False
    """    
    total = 0;
    for i in range(len(table) - 1):
        for j in range(len(table) - 1):
            if wanted_sum == table[i][j] + table[i + 1][j] + table[i][j + 1] + table[i + 1][j + 1]:
                return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()