from typing import List


def please_delete(messages: List[str]):
    """messages a list that represents messages in a group chat, sorted chronologically,
    (a message sent first would have a lower index than the later ones).
    
    If someone sends the message 'delete', the previous message should be removed.
    Modify the original list.
    
    >>> msg_1 = ['Conrad has small pp', 'delete', 'Hello', 'How is everyone doing?', 'Also, how was yesterday, Conrad?', 'delete']
    >>> please_delete(msg_1)
    >>> msg_1
    ['delete', 'Hello', 'How is everyone doing?', 'delete']
    >>> msg_2 = ['delete', 'Hello', 'How is everyone doing?', 'Also, how was yesterday, Conrad?', 'delete', 'delete', 'why']
    >>> please_delete(msg_2)
    >>> msg_2
    ['delete', 'Hello', 'How is everyone doing?', 'delete', 'why']
    """
    for i in range(1, len(messages)): 
        #we start at 1 because we want to avoid errors if the first message is delete.
        if messages[i] == 'delete':
            messages[i - 1] = None 
        #Usually, we don't want to remove values while iterating over a list, since it can cause
        #some problems, like shifting index.
        #So, we turn the values we don't want into something that's not a string, to easily remove it later. 
        #(we can use something like int or bool here too)
    while None in messages:
        messages.remove(None)
            
    

def DELETE_DELETE_PLEASE_GUYS_holy_fuck_you_guys_are_bad_friends(messages: List[str], delete_threshold):
    """messages a list that represents messages in a group chat, sorted chronologically,
    (a message sent first would have a lower index than the later ones).
    
    If someone sends the message 'delete' delete_threshold times consecutively, the message
    before them should be removed.
    
    For example, if the delete_threshold is 3, it would take Conrad to type 'delete' 3 times before
    the previous message is removed.
    
    >>> msg_1 = ['Conrad has small pp', 'delete', 'Hello', 'How is everyone doing?', 'Also, how was yesterday, Conrad?', 'delete', 'delete', 'delete']
    >>> DELETE_DELETE_PLEASE_GUYS_holy_fuck_you_guys_are_bad_friends(msg_1, 3)
    >>> msg_1
    ['Conrad has small pp', 'delete', 'Hello', 'How is everyone doing?', 'delete', 'delete', 'delete']
    >>> msg_2 = ['delete', 'delete', 'delete', 'Hello', 'How is everyone doing?', 'Also, how was yesterday, Conrad?', 'delete', 'delete', 'delete', 'delete', 'delete', 'why']
    >>> DELETE_DELETE_PLEASE_GUYS_holy_fuck_you_guys_are_bad_friends(msg_2, 2)
    >>> msg_2
    ['delete', 'delete', 'Hello', 'How is everyone doing?', 'delete', 'delete', 'why']
    """

    for i in range(1, len(messages)):
        #if delete_threshold is 3, this is like saying counting from i to i + 2 (cus we exclude i + 3)
        if messages[i:i + delete_threshold].count('delete') == delete_threshold: 
            messages[i - 1] = None
    while None in messages:
        messages.remove(None)


if __name__ == '__main__':
    import doctest
    doctest.testmod()