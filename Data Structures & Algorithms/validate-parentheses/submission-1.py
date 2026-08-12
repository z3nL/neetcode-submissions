class Solution:
    def isValid(self, s: str) -> bool:
        closes = {')', '}', ']'}
        toOpen = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if stack and c in closes:
                if stack[-1] != toOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack)==0