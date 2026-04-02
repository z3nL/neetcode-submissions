class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        res = []
        n = len(nums)
        cur = []

        def bt(used):
            # Base case: cur is a complete permutation
            if len(cur) == n:
                res.append(cur[:])
            
            # Iterate all indices of nums
            for num in nums:
                # Index was already used
                if num in used:
                    continue
                
                # New path to explore
                cur.append(num); used.add(num) 
                bt(used)
                cur.pop(); used.remove(num)

        bt(set())
        return res
        