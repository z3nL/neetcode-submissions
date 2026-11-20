class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList) 

        if endWord not in wordList:
            return 0

        pattern_map = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i]+'*'+w[i+1:]
                pattern_map[pattern].append(w)
        
        q = deque([beginWord])
        wordList.add(beginWord)
        level = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w not in wordList:
                    continue
                wordList.remove(w)
                if w == endWord:
                    return level
                for i in range(len(w)):
                    pattern = w[:i]+'*'+w[i+1:]
                    if pattern in pattern_map:
                        q += pattern_map[pattern]
            level += 1
        return 0

        