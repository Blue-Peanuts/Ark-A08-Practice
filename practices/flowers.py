from typing import Dict

def pick_flowers(friend_interests: Dict[str, str], flowers: Dict[str, int]) -> Dict[str, int]:
    """friends_interests is a dictionary with keys representing people's names, and values
    representing colors they like. flowers represent a dictionary with flower colors as keys
    but the quantity as values.
    
    Everyone will pick all, (and only), the flowers with the colors that they like.
    
    Assuming EACH PERSON LIKES DIFFERENT COLORS,
    return a dictionary containing everyone's names as keys,
    and the quantity of the flowers each of them picked as values.
    
    >>> interests_1 = {'Cheryl': 'White', 'Ashley': 'Black', 'Justin': 'Blue', 'Christina': 'Red'}
    >>> flowers_1 = {'White': 1, 'Red': 3, 'Orange': 2}
    >>> pick_flowers(interests_1, flowers_1)
    {'Cheryl': 1, 'Ashley': 0, 'Justin': 0, 'Christina': 3}
    """
    
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()