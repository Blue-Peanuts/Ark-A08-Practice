from typing import TextIO, List
def kill_log(log_file: TextIO) -> List[str]:
    """Return a list of survivors after the
    scenarios in log_file occured.
    Each line in log_file will contain
    A name followed by action and another name.
    Actions can be 'attack' or 'protect'
    
    if someone attacks someone, the other person dies.
    But if the person has someone protecting them, the person doesn't die.
    For example 
    Ark protect Conrad
    Sigmund attack Conrad
    No one would die in this case
    
    
    But if the person doing the protecting changes their target, or dies, the person being protected doesn't have protection anymore.
    If a person acts when they should be dead, return 'Fake kill log' instead.
    
    For example
    Ark attack Conrad
    Conrad protect Justin
    Should return 'Fake kill log' since Conrad should be dead right now
    
    You also cannot kill or protect a dead person
    For example
    Ark attack Conrad
    Sigmund attack Conrad
    Should return 'Fake kill log' since Conrad should be dead already
    
    
    >>> file = open('kill_log_1.txt', 'r')
    >>> ans = kill_log(file)
    >>> ans.sort()
    >>> ans
    ['Cheryl', 'Conrad', 'Shaul']
    >>> file = open('kill_log_2.txt', 'r')
    >>> ans = kill_log(file)
    >>> ans.sort()
    >>> ans
    ['Conrad', 'Shaul']
    >>> file = open('kill_log_3.txt', 'r')
    >>> ans = kill_log(file)
    >>> ans.sort()
    >>> ans
    ['Conrad', 'Ivy', 'Shaul']
    >>> file = open('kill_log_4.txt', 'r')
    >>> ans = kill_log(file)
    >>> ans
    'Fake kill log'
    >>> file = open('kill_log_5.txt', 'r')
    >>> ans = kill_log(file)
    >>> ans.sort()
    >>> ans
    ['Ark', 'Conrad', 'Ivy', 'Patrick', 'Shaul']
    >>> file = open('kill_log_6.txt', 'r')
    >>> ans = kill_log(file)
    >>> ans
    'Fake kill log'
    """

   people = {}  # generally the values are [alive/dead, protected/unprotected, if protected then who]
    for line in log_file.readlines():
        line = line.strip('\n').split()
        if line[0] not in people:
            people[line[0]] = ['alive', 'unprotected', '']
        if line[1] == 'attack':
            if line[2] not in people or people[line[2]][1] == 'unprotected':
                people[line[2]] = ['dead', 'unprotected', '']
                for person in people:
                    if people[person][2] == line[2]:
                        people[person][1], people[person][2] = 'unprotected', ''
            elif people[line[2]][0] == 'dead':
                return 'Fake kill log'
        else:
            if line[2] not in people:
                people[line[2]] = ['alive', '', '']
            people[line[2]][1], people[line[2]][2] = 'protected', line[0]
            for person in people:
                if person != line[2] and people[person][2] == line[0]:
                    people[person][1], people[person][2] = 'unprotected', ''
        if people[line[0]][0] == 'dead':
            return 'Fake kill log'

    result = []
    for person in people:
        if people[person][0] == 'alive':
            result.append(person)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
