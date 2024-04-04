'''
88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, 
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
'''

def merge(self, nums1, m, nums2, n):
    if (len(nums1) == m + n) and (len(nums2) == n) and (0 <= m) and (n <= 200) and (1 <= m + n <= 200):
        valido = True

        for i in nums1:
            if i <= -10**9:
                valido = False
            elif i <= -10**9:
                valido = False

        for i in nums2:
            if i <= -10**9:
                valido = False
            elif i <= -10**9:
                valido = False

        if valido:

            c = []

            for i in range(m):
                c.append(nums1[i])

            for i in range(n):
                c.append(nums2[i])
                
            nums1[:] = sorted(c)         
            return print(nums1)
        else:
            print("ERRO02")
    else:
        print("ERRO")

'''
Runtime: 18ms
Memory: 11.55MB
'''