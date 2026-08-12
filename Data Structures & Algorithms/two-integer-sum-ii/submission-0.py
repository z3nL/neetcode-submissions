class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            cur = numbers[i] + numbers[j]
            if cur > target:
                j -= 1
            elif cur < target:
                i += 1
            else:
                return [i+1, j+1]
        