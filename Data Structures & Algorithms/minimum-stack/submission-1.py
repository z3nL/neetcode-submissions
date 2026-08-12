class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.ms or val <= self.ms[-1]:
            self.ms.append(val)

    def pop(self) -> None:
        r = self.s.pop()
        if self.ms and r == self.ms[-1]:
            self.ms.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]
