import collections
from typing import Deque


word1 = "ab"
word2 = "pqrs"


def mergeAlternately(word1: str, word2: str):
    merge: Deque = collections.deque()

    for i in range(min(len(word1), len(word2))):
        merge.append(word1[i] + word2[i])

    return "".join(merge) + word1[i + 1 : :] + word2[i + 1 : :]


print(mergeAlternately(word1, word2))
