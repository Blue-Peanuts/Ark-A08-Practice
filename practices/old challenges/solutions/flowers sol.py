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

    to_return = {}
    
    for friend in friend_interests:
        #get() is better than just straight up using flowers[interest],
        #since it can avoid errors by putting a second argument there to be
        #the default return incase it doesn't find a value.
        #Meaning if interest is not a key in flowers, it would return 0 instead
        to_return[friend] = flowers.get(friend_interests[friend], 0) 
    return to_return


if __name__ == '__main__':
    import doctest
    doctest.testmod()