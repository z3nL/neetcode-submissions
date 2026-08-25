class Trie:
    def __init__(self):
        self.nxt = [None]*26
        self.isWord = False

class PrefixTree:
    
    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.nxt[ord(c)-ord('a')] is None:
                cur.nxt[ord(c)-ord('a')] = Trie()
            cur = cur.nxt[ord(c)-ord('a')]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.nxt[ord(c)-ord('a')] is None:
                return False
            cur = cur.nxt[ord(c)-ord('a')]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if cur.nxt[ord(c)-ord('a')] is None:
                return False
            cur = cur.nxt[ord(c)-ord('a')]
        return cur.isWord or any(cur.nxt)   
        