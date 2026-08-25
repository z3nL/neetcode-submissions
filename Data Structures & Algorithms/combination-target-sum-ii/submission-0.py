class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        self.res = []
        
        def bt(i, s, arr):
            if i >= len(nums) or s >= target:
                if s == target: self.res.append(list(arr))
                return
            
            arr.append(nums[i])
            bt(i+1, s+nums[i], arr)
            arr.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            bt(i+1, s, arr)

        bt(0, 0, [])
        return self.res