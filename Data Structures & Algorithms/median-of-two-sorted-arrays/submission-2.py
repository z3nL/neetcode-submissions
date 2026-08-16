class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # want nums 2 to give out first
        if n > m:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        need = (m+n)//2 + 1
        res = []
        
        i, j = 0, 0
        while need > 0:
            if i < m and (j >= n or nums1[i] < nums2[j]):
                if need < 3: res.append(nums1[i])
                i += 1
            else:
                if need < 3: res.append(nums2[j])
                j += 1
            need -= 1

        return (res[-1]+res[-2])/2 if (m+n)%2 == 0 else res[-1]