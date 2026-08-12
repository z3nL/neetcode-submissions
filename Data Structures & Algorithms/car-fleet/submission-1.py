class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(list(zip(position, speed)), key=lambda x: x[0], reverse=True)
        s =  []
        for car in cars:
            tta = (target-car[0])/car[1]
            if not s or tta > s[-1]:
                s.append(tta)
        return len(s)