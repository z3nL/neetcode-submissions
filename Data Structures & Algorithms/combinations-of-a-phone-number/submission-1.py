class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        phone = {
            '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z'],
        }
        
        res = []
        def bt(cur, i):
            if i == len(digits):
                res.append(''.join(cur[:]))
                return
            
            for digit in phone[digits[i]]:
                cur.append(digit)
                bt(cur, i+1)
                cur.pop()
        
        bt([], 0)
        return res