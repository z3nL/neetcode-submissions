class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range (0, len(nums)):
            cur = target-nums[i]
            if (cur in s):
                return [s[cur], i]
            s[nums[i]] = i
