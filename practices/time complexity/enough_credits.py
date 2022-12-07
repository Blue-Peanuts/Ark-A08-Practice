from typing import Tuple, List

# Try to guess what the best case and worst case time complexity is for this function.
# Also guess the number of comparisons
# Then check your answer with the answer file in the same folder I provided.

def enough_credits(courses: List[Tuple[str, float]], needed_credits: float) -> bool:
    """Return True iff after taking all the courses in courses list,
    you will have enough credits according to needed_credits.
    
    >>> enough_credits([('a08', 0.5), ('a31', 0.5), ('a67', 1.0)], 2)
    True
    >>> enough_credits([('a08', 0.5), ('a31', 0.5), ('a67', 1.0)], 3)
    False
    >>> enough_credits([('a08', 0.5), ('a31', 0.5), ('a67', 1.0)], 0)
    True
    >>> enough_credits([], 0)
    True
    >>> enough_credits([], 1)
    False
    """
    credits = 0
    i = 0
    while i < len(courses) and credits < needed_credits:
        credits += courses[i][1]
        i += 1
    return credits >= needed_credits


if __name__ == '__main__':
    import doctest
    doctest.testmod()