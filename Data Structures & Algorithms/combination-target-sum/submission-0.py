class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        
        def bt(i, s, arr):
            if i == len(nums) or s >= target:
                if s == target: self.res.append(list(arr))
                return
            
            arr.append(nums[i])
            bt(i, s+nums[i], arr)
            arr.pop()
            bt(i+1, s, arr)

        bt(0, 0, [])
        return self.res