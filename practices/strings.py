def delete(text: str, start_index: int, last_index: int) -> str:
    """Return text with characters from index
    start_index to last_index removed (including the character at last_index)

    >>> delete('hippo', 1, 2)
    'hpo'
    >>> delete('soccer', 1, 2)
    'hpo'
    """
    pass


def delete_when_substring(text: str, substring: str) -> str:
    """Return text with only the characters before
    substring appears
    
    You can assume that substring is in text
    
    >>> delete_when_substring("Apple Pie", "Pie")
    'Apple '
    >>> delete_when_substring("Pineapple", "nea")
    'Pi'
    
    """
    pass


def delete_after_substring(text: str, substring: str) -> str:
    """Return text with the characters after 
    the substring removed
    
    You can assume that substring is in text
    
    >>> delete_after_substring("Apple Pie", "Pie")
    'Apple Pie'
    >>> delete_after_substring("Pineapple", "nea")
    'Pinea'
    
    """
    pass


def is_binary_string(text: str) -> bool:
    """Return true if and only if text only contains
    0s and 1s. An empty string is not a binary string.
    
    >>> is_binary_string('')
    False
    >>> is_binary_string('Hipp0')
    False
    >>> is_binary_string('00111000')
    True
    """
    pass

VOWELS = 'aeiouAEIOU'

def check_if_string_same_ignore_vowels(text1: str, text2: str) -> bool:
    """Return true if and only if text1 and text2 are the same, 
    ignoring vowels
    
    >>> check_if_string_same_ignore_vowels('bat','bet')
    True
    >>> check_if_string_same_ignore_vowels('boss', 'best')
    False
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()