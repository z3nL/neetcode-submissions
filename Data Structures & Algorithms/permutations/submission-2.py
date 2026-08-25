class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False]*len(nums)

        def bt(cur):
            if len(cur) == len(nums):
                self.res.append(list(cur))
            
            for i in range(len(nums)):
                if not self.used[i]:
                    cur.append(nums[i])
                    self.used[i] = True
                    bt(cur)
                    cur.pop()
                    self.used[i] = False
        
        bt([])
        return self.res