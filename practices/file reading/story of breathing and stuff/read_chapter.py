from typing import TextIO
chap1_ans = "Justin sharted so hard\nhe launched himself to the moon\n"
chap2_ans = "Justin can't breathe in space\nSo he had to steal Conrad's gas tank\nin 3 seconds to survive\n"
chap3_ans = "Conrad doesn't have oxygen\noxygen = live\nno oxygen = death\n"
chap4_ans = "Everyone\nCries\nOver Connor's death"

def read_chapter(chapter: int, story_file: TextIO) -> str:
    """Return the contents of chapter chapter from story_file.
    Exclude the line with chapter header
    Look at story.txt for more context
    
    Precondition: chapter is a valid chapter in story_file

    >>> file = open('story.txt', 'r')
    >>> read_chapter(1, file) == chap1_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_chapter(2, file) == chap2_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_chapter(3, file) == chap3_ans
    True
    >>> file = open('story.txt', 'r')
    >>> read_chapter(4, file) == chap4_ans
    True
    """
    to_return = ''
    story = story_file.readlines()
    i = 0
    found_chapter = False
    while i < len(story) and 'Chapter ' + str(chapter + 1) not in story[i]:
        if found_chapter:
            to_return += story[i]
        if 'Chapter ' + str(chapter) in story[i]:
            found_chapter = True
        i += 1
    return to_return


if __name__ == '__main__':
    import doctest
    doctest.testmod()