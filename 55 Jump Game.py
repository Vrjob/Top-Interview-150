'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
'''
def canJump(self, nums):
    max_reachable = 0  # Initialize the maximum index reachable so far
    
    for i in range(len(nums)):
        if i > max_reachable:
            return False  # If the current index is not reachable, return False
        max_reachable = max(max_reachable, i + nums[i])  # Update the maximum reachable index
        
        if max_reachable >= len(nums) - 1:
            return True  # If the last index is reachable, return True
    
    return False


            


        