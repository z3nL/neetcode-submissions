class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = list()
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j, k = i+1, n-1
            while j < k:
                cur = nums[j] + nums[k]
                if cur > target:
                    k -= 1
                elif cur < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j += 1
                    k -= 1
        return res