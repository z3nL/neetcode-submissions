class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i+1 < len(intervals):
            cs, ce = intervals[i]
            ns, ne = intervals[i+1]
            if ce >= ns:
                intervals.pop(i+1)
                intervals[i] = [cs, max(ce, ne)]
            else:
                i += 1
        return intervals