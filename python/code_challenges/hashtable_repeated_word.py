import re
from data_structures.hashtable import Hashtable


def first_repeated_word(string):

    if len(string) == 0:
        return None

    hash_map = Hashtable()
    lowered = string.lower()
    words_array = re.findall(r'\b[\w\?.-]+\b', lowered)

    for word in words_array:
        if hash_map.has(word):
            return word
        else:
            hash_map.set(word, word)

    return None
