class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        n = len(nums)

        def bt(cur, used):
            # Base case: cur is a complete permutation
            if len(cur) == n:
                res.append(cur[:])
            
            # Iterate all indices of nums
            for i in range(n):
                # Index was already used
                if i in used:
                    continue
                
                # New path to explore
                cur.append(nums[i]); used.add(i) 
                bt(cur, used)
                cur.pop(); used.remove(i)

        bt([], set())
        return res
        