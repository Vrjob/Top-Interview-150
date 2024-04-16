"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum1(self, nums, target):
    i = 0

    while i <= len(nums):
        j = 0
        while j <= len(nums):    
            if nums[i] + nums[j] == target:
                return [i,j]
            j += 1
        i += 1

def twoSum2(self, nums, target):
    num_index_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index_map:
            return [num_index_map[complement], i]
        num_index_map[num] = i
    return []
    