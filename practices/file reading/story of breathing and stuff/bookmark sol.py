from typing import TextIO


chap1_ans = "Chapter 1 - Justin sharted\nJustin sharted so hard\nhe launched himself to the moon\nChapter 2 - Justin in space\nJustin can't breathe in space\nSo he had to steal Conrad's gas tank\nin 3 seconds to survive\nChapter 3 - Conrad fucking dies\nConrad doesn't have oxygen\noxygen = live\nno oxygen = death\nChapter 4 - Everyone cries\nEveryone\nCries\nOver Connor's death"
chap2_ans = "Chapter 2 - Justin in space\nJustin can't breathe in space\nSo he had to steal Conrad's gas tank\nin 3 seconds to survive\nChapter 3 - Conrad fucking dies\nConrad doesn't have oxygen\noxygen = live\nno oxygen = death\nChapter 4 - Everyone cries\nEveryone\nCries\nOver Connor's death"
chap3_ans = "Chapter 3 - Conrad fucking dies\nConrad doesn't have oxygen\noxygen = live\nno oxygen = death\nChapter 4 - Everyone cries\nEveryone\nCries\nOver Connor's death"
chap4_ans = "Chapter 4 - Everyone cries\nEveryone\nCries\nOver Connor's death"
chap5_ans = "end"


def read_from_bookmark(chapter: int, story_file: TextIO) -> str:
    """Return the entire story starting from chapter chapter.
    Look at story.txt to see what it looks like.
    If the chapter doesn't exist, return 'end'

    >>> file = open('story.txt', 'r')
    >>> read_from_bookmark(1, file) == chap1_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_from_bookmark(2, file) == chap2_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_from_bookmark(3, file) == chap3_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_from_bookmark(4, file) == chap4_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_from_bookmark(5, file) == chap5_ans
    True
    """
    story = story_file.read()
    if 'Chapter ' + str(chapter) in story:
        return story[story.find('Chapter ' + str(chapter)): ]
    return 'end'
    


if __name__ == '__main__':
    import doctest
    doctest.testmod()