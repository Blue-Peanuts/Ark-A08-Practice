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
# Also guess the number of inner loops ran
# Then check your answer with the answer file in the same folder I provided.
# Let N be the length/width of the table in this case

def sum_table(table: List[List[int]]) -> int:
    """Sum all the numbers in table
    The table is a square (length = width)

    >>> sum_table(THREE_BY_THREE)
    47
    >>> sum_table(FOUR_BY_FOUR)
    53
    >>> sum_table(FIVE_BY_FIVE)
    94
    """    
    total = 0;
    for row in table:
        for item in row:
            total += item
    return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()