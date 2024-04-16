"""

"""

def shuffle(self, nums, n):
    nums1 = nums[:(int(len(nums)/2))]
    nums2 = nums[(int(len(nums)/2)):]
    newNums = []
    i = 0

    while i < int(len(nums)/2):
        newNums.append(nums1[i])
        newNums.append(nums2[i])
        i += 1

    return newNums 


nums = [2,5,1,3,4,7]
n = 3

shuffle(0, nums, n)