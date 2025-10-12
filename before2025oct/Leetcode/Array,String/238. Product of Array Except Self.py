def productExceptSelf(nums: list[int]) -> list[int]:
    answer = []
    # print(nums[2])
    a = 1
    for i in range(len(nums)):
        a *= nums[i]

    for i in nums:
        if i == 0:
            answer.append(a)
        else:
            answer.append(a // i)

    return answer


print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([-1, -1, 0, -3, -3]))

# Output: [24,12,8,6]

""" 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
