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
    
    You also cannot kill a dead person
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
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()