nums = [1, 2, 3, 1]

## Hast set ( O(n) )


def containsDuplicate(nums) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


## Sort


class Solution:
    def containsDuplicate(nums) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False


## Brute Force ( O(n^2))


def containsDuplicate(nums) -> bool:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True

    return False


containsDuplicate(nums)
