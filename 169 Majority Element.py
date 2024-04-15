'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Constraints:

n == nums.length
1 <= n <= 5 * 104
-10^9 <= nums[i] <= 10^9
'''

def majorityElement(self, nums):
    if 0 < len(nums) <= (5 * 10**4):
        for i in nums:

            if (-10**9 <= i <= 10**9):

                if nums.count(i) > (len(nums)/2):
                    c = i
                    return(c)

