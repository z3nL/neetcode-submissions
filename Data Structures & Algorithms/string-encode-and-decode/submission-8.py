class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'machine2'
        c = ''
        for s in strs[:-1]:
            c += s + 'machine1'
        return c + strs[-1]

    def decode(self, s: str) -> List[str]:
        if s == 'machine2':
            return []
        return s.split('machine1')
