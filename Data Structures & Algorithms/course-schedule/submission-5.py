class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        seen = set()
        def validate(course):
            if course not in prereqs:
                return True

            seen.add(course)
            for prereq in prereqs[course]:
                if prereq in seen or not validate(prereq):
                    return False
            seen.remove(course)

            # This course is validated, we can remove it from the map
            del prereqs[course]
            return True
        
        return all(validate(course) for course in range(numCourses))
        