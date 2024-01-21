import collections
from typing import Deque


def merge(nums1: [int], m: int, nums2: [int], n: int):
    answer: Deque = collections.deque()

    answer = nums1[:m] + nums2[:n]

    for i in range(len(answer)):
        nums1[i] = answer[i]

    nums1.sort()
    print(nums1)


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

a = [1, 2, 3]
print(a[:2])
