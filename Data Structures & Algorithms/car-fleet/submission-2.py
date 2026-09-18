class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), key=lambda x: x[0], reverse=True)
        res = []

        for p, s in cars:
            if not res or (target-p)/s > res[-1]:
                res.append((target-p)/s)

        return len(res)