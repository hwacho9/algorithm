import collections
import random


def groupAnagrams(strs: [str]):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams["".join(sorted(word))].append(word)

    print(list(anagrams.values()))


# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# groupAnagrams(strs)

# print(27020856 % 12)
