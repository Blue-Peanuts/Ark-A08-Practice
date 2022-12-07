# Try to guess what the best case and worst case time complexity is for this function.
# Also guess the number of comparisons
# Then check your answer with the answer file in the same folder I provided.

def is_palindrome(word :str) -> bool:
    """Return True iff the word is a palindrome.
    
    Precondition: len(word) > 0
    
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('giraffe')
    False
    >>> is_palindrome('asdfghjhgfdsa')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('abbbfa')
    False
    >>> is_palindrome('abcdef')
    False
    """
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()