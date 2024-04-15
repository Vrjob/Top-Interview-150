"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
def rotate1(self, nums, k):
    i = 0
    k = k % len(nums)
    while i < k:
        amz = nums[-1]
        nums.pop()
        nums.insert(0, amz)
        i += 1

    return nums

def rotate2(self, nums, k):
    k = k % len(nums)  # Lidando com k maior que o comprimento da lista
    nums[:] = nums[-k:] + nums[:-k]  # Rotacionando a lista usando slicing
    return nums