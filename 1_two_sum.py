"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

#SUCCESS
def two_sum(target, nums):
    for i in nums:
        for j in range(nums.index(i) + 1, len(nums)):
            if i + nums[j] == target:
                return [nums.index(i), j]

nums = [2,5,5,11]
target = int(input("integer target: "))
print(two_sum(target, nums))

