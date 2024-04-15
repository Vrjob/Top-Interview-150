'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, 
you need to do the following things:

    > Change the array nums such that the first k elements of nums 
    contain the unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    > Return k.

Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

def removeDuplicates(self, nums):
    if len(nums) >= 1  and len(nums) <= 3**104:
        valido = True

        for i in nums:
            if (i < -100) or (i > 100):
                valido = False

        if valido:        
            c = sorted(set(nums[:]))
            nums[:] = c
            print(nums)


removeDuplicates(0,[1,0,-399,2,3,4,4,4,4,8])
