class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                s.append(t)
            else:
                r, l = int(s.pop()), int(s.pop())
                if t == '+':
                    c = l + r
                if t == '-':
                    c = l - r
                if t == '*':
                    c = l * r
                if t == '/':
                    c = l / r
                s.append(c)
        return int(s[0])