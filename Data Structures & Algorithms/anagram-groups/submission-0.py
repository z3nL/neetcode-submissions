class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for s in strs:
            buckets[''.join(sorted(s))].append(s)
        return list(buckets.values())
        