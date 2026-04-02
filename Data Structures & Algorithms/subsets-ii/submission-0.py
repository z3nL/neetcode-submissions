class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        res = []

        def bt(cur, i):
            if i == n:
                res.append(cur[:])
                return

            cur.append(nums[i])
            bt(cur, i+1)
            cur.pop()
            
            # If you skip a value, skip to the next different value
            j = i+1
            while j < n and nums[j] == nums[i]:
                j += 1
            bt(cur, j)

        bt([], 0)
        return res
        