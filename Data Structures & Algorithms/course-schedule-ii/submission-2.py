class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        ready = set(range(numCourses))

        prereqs = defaultdict(set)
        children = defaultdict(set)
        for a, b in prerequisites:
            if a in ready:
                ready.remove(a)
            prereqs[a].add(b)
            children[b].add(a)
        
        q = deque(ready)
        while q:
            cur = q.popleft()
            res.append(cur)
            numCourses -= 1
            for child in children[cur]:
                prereqs[child].remove(cur)
                if not prereqs[child]:
                    q.append(child)

        return res if numCourses == 0 else []