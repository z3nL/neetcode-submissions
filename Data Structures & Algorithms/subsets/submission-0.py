class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.cur = []

        def bt(i):
            if i == len(nums):
                self.res.append(list(self.cur))
                return
            
            self.cur.append(nums[i])
            bt(i+1)
            self.cur.pop()
            bt(i+1)

        bt(0)
        return self.res