"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
def numIdenticalPairs1(self, nums):
    count = 0

    j = 0
    while j in range(len(nums)):
        i = 0
        while i in range(len(nums)):
            if nums[i] == nums[j] and i < j :
                count += 1  
            
            i +=1
        j +=1

    return count

def numIdenticalPairs2(self, nums):
    
    count_map = {}
    
    for num in nums:
        if num in count_map:
            count_map[num] +=1
        else:
            count_map[num] =1
    # {1: 3, 2: 1, 3: 2}
    print(count_map)
    no_of_good_pairs = 0
    for key,val in count_map.items():
        no_of_good_pairs += val * (val-1) //2
    
    return no_of_good_pairs