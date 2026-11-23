class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '!Nothing!'
        return "NEETCODE150".join(strs)

    def decode(self, s: str) -> List[str]:
        if s is '!Nothing!':
            return []
        return s.split("NEETCODE150")
