def delete(text: str, start_index: int, last_index: int) -> str:
    """Return text with characters from index
    start_index to last_index removed (including the character at last_index)

    >>> delete('hippo', 1, 2)
    'hpo'
    >>> delete('soccer', 1, 2)
    'scer'
    """

    return text[0: start_index] + text[last_index + 1: ]


def delete_when_substring(text: str, substring: str) -> str:
    """Return text with only the characters before
    substring appears
    
    You can assume that substring is in text
    
    >>> delete_when_substring("Apple Pie", "Pie")
    'Apple '
    >>> delete_when_substring("Pineapple", "nea")
    'Pi'
    """

    return text[0: text.find(substring)]


def delete_after_substring(text: str, substring: str) -> str:
    """Return text with the characters after 
    the substring removed
    
    You can assume that substring is in text
    
    >>> delete_after_substring("Apple Pie", "Pie")
    'Apple Pie'
    >>> delete_after_substring("Pineapple", "nea")
    'Pinea'
    
    """

    return text[0: text.find(substring) + len(substring)]
 ######## Alternative Solution ############################
 ##
 ## return text[0: text.find(substring)] + substring


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

    return len(text) > 0 and text.count('0') + text.count('1') == len(text)
 ######## Alternative Solution ############################
 ##
 ## if len(text) == 0:
 ##     return False
 ## for ch in text:
 ##     if ch not in '01':
 ##         return False
 ## return True


VOWELS = 'aeiouAEIOU'

def check_if_string_same_ignore_vowels(text1: str, text2: str) -> bool:
    """Return true if and only if text1 and text2 are the same, 
    ignoring vowels
    
    >>> check_if_string_same_ignore_vowels('bat','bet')
    True
    >>> check_if_string_same_ignore_vowels('boss', 'best')
    False
    """

    for vowel in VOWELS:
        text1 = text1.replace(vowel, '')
        text2 = text2.replace(vowel, '')
    return text1 == text2
 ####### Alternative Solution ############################
 ## new_text1 = ''
 ## new_text2 = ''
 ## for ch in text1:
 ##     if ch not in VOWELS:
 ##         new_text1 += ch
 ## for ch in text2:
 ##     if ch not in VOWELS:
 ##         new_text2 += ch
 ## return new_text1 == new_text2


if __name__ == '__main__':
    import doctest
    doctest.testmod()