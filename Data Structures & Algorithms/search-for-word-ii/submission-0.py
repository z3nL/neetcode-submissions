class TrieNode:
    def __init__(self):
        self.next = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []

        # Build a trie
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.next:
                    cur.next[c] = TrieNode()
                cur = cur.next[c]
            cur.word = word

        res = []
        m, n = len(board), len(board[0])

        def bt(i, j, cur):
            
            c = board[i][j]
            nxt = cur.next.get(c, None)

            if not nxt:
                return
            
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None
            
            board[i][j] = '#'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+dx, j+dy
                if 0<=ni<m and 0<=nj<n:
                    bt(ni, nj, nxt)
            board[i][j] = c

        cur = root
        for i in range(m):
            for j in range(n):
                bt(i, j, cur)
        
        return res
        