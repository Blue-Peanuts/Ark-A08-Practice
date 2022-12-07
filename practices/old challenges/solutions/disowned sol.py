from typing import List


def is_disowned(grades: List[int]) -> bool:
    """Return True if and only if the given grades grades,
    is of a student who is getting disowned by Ark.
    A student gets disowned by Ark if they get under 50
    in ANY one of the courses, or the average grade is under 75.
    
    Preconditions: grades composes of non-negative integers
                   not exceeding 100.
    
    >>> is_disowned([40, 100, 90, 80])
    True
    >>> is_disowned([65, 70, 85, 70])
    True
    >>> is_disowned([100, 70, 85, 70])
    False
    """

    for grade in grades:
        if grade < 50:
            return True
    return sum(grades) / len(grades) < 75


def num_disowned(student_grades: List[List[int]]) -> int:
    """Return the amount of students getting disowned, considering
    each element in student_grades represent the grades of a student.

    >>> num_disowned([[10, 100, 90, 80], [65, 70, 85, 70], [100, 70, 85, 70]])
    2
    """

    count = 0
    for grades in student_grades:
        if is_disowned(grades):
            count += 1
    return count


if __name__ == '__main__':
    import doctest
    doctest.testmod()