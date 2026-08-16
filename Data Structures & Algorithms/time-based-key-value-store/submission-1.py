class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.s.get(key, None)
        if not arr:
            return ""
        
        l, r = 0, len(arr)-1
        while l <= r:
            m = (l+r) // 2
            if arr[m][1] < timestamp:
                l = m + 1
            elif arr[m][1] > timestamp:
                r = m - 1
            else:
                return arr[m][0]
        return arr[r][0] if arr[r][1] < timestamp else ""
