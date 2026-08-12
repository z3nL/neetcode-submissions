class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0]*n

        s = []
        for j in range(n):
            while s and temperatures[j] > temperatures[s[-1]]:
                i = s.pop()
                res[i] = j-i
            s.append(j)
        
        return res