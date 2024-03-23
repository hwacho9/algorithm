from collections import deque


def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    left = 0
    zero = 0

    for i in range(len(nums)):
        if nums[left] == 0:
            # print(nums)
            nums.pop(left)
            # nums.append(0)
            # left += 1
            zero += 1
            # print(nums, i)
        else:
            left += 1
            # print(nums, i, "t")
    # while left < right:
    #     if nums[left] is 0 or nums[right] is 0:

    for i in range(zero):
        nums.append(0)

    return nums


print(moveZeroes([0, 1, 0, 3, 12]))
# Output: [1,3,12,0,0]
print(moveZeroes([0, 0, 1]))
# expected [1,0,0]
