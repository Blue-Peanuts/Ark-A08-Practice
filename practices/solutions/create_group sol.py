from typing import List


def create_group(people: List[str]) -> List[List[str]]:
    """Seperate people into groups, containing only people with the same
    first letter of the name, (e.g. Ark and Andy).
    
    The groups and name should be in alphabetical order. (use list.sort() function)
    
    >>> create_group(['Ark', 'Conrad', 'Christina', 'Patrick', 'Andy'])
    [['Andy', 'Ark'], ['Christina', 'Conrad'], ['Patrick']]
    """
    
    people.sort() #now names like Andy and Ark will be next to eachother, allowing for easier comparison
    current_group = []
    to_return = []
    for person in people:
        #if the current group we are building is empty, or person has the same matching first character with others in curr_group
        if len(curr_group) == 0 or person[0] == current_group[0][0]:
            curr_group.append(person)
        else: #if called, the current_group is finished because there are no more people with same character, so we append it to the answer, and build a new group
            to_return.append(current_group)
            curr_group = [person]
    to_return.append(curr_group) #don't leave the final group alone, we haven't appended it
    return to_return


if __name__ == '__main__':
    import doctest
    doctest.testmod()