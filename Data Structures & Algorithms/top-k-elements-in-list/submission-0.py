class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        return [x[0] for x in sorted(res.items(), key=lambda x: x[1], reverse=True)[:k]]