from typing import Dict, TextIO

def get_food_after_log(log_file: TextIO) -> Dict[str, Dict[str, int]]:
    """Return a dictionary representing food on the table
    after the actions in log_file is taken.
    
    The first line in the file tells you what's on the menu
    The rest tells you actions
    
    For example:
    Menu: Pork, Fish, Shrimp
    Conrad orders Shrimp, Pork
    Conrad eats Pork
    Shaul orders Fish
    
    Should return {Conrad: {Pork: 0, Shrimp: 1, Fish: 0}, Shaul: {Fish: 0}}
    
    Note that even though Conrad did not eat nor ordered Fish, Fish should still be a key in Conrad's dictionary.
    
    >>> file = open('log_1.txt', 'r')
    >>> get_food_after_log(file) == {'Conrad': {'Shrimp': 0, 'Pork': 1, 'Chicken': 0, 'Mushroom': 0}, 'Josephine': {'Shrimp': 0, 'Pork': 0, 'Chicken': 1, 'Mushroom': 0}}
    True
    >>> file = open('log_2.txt', 'r')
    >>> get_food_after_log(file) == {'Conrad': {'Shrimp': 0, 'Pork': 0, 'Chicken': 0}, 'Josephine': {'Shrimp': 0, 'Pork': 0, 'Chicken': 1}}
    True
    >>> file = open('log_3.txt', 'r')
    >>> get_food_after_log(file) == {'Conrad': {'Shrimp': 0, 'Pork': 0, 'Chicken': 0, 'Fish': 0, 'Noodles': 1}, 'Josephine': {'Shrimp': 0, 'Pork': 1, 'Chicken': 3, 'Fish': 0, 'Noodles': 0}, 'Kate': {'Shrimp': 0, 'Pork': 0, 'Chicken': 0, 'Fish': 1, 'Noodles': 0}}
    True
    """
    dic = {}
    log = log_file.readlines()
    menu = log[0][log[0].find(' ') + 1:].strip().split(', ')
    
    for line in log[1:]:
        person = line.split(' ')[0]
        action = line.split(' ')[1]
        foods = line.split()[2:]
        if person not in dic:
            dic[person] = {}
            for food in menu:
                dic[person][food] = 0
        for food in foods:
            food = food.strip(',')
            if action == 'orders':
                dic[person][food] += 1
            if action == 'eats':
                dic[person][food] -= 1
    return dic

if __name__ == '__main__':
    import doctest
    doctest.testmod()