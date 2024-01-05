import collections
import re


def isPalindrome(s: str) -> bool:
    # strs = collections.deque()

    # for char in s:
    #     if char.isalnum():  #
    #         strs.append(char.lower())

    # while len(strs) > 1:
    #     if strs.popleft() != strs.pop():
    #         return False

    # return True

    s = s.lower()

    s = re.sub("[^a-z0-9]", "", s)  #

    return s == s[::-1]


A = str(input())

if isPalindrome(A) is True:
    print(True)
else:
    print(False)
