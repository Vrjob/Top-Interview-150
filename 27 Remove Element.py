'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

   >Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
    The remaining elements of nums are not important as well as the size of nums.
   >Return k.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
'''

def removeElement(self, nums, val):
    if (0 <= len(nums) <= 100) and (0 <= val <= 100):
        valido = True

        for i in nums:
            if (i < 0) or (i > 50):
                valido = False

        if valido:
            nums[:] = [x for x in nums if x != val]

'''
Runtime: 15ms
Memory: 11.58MB
'''