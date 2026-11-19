class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        resolved = {}
        def validate(course, seen): #, path):
            if course in resolved:
                return resolved[course]
            if course not in prereqs:
                resolved[course] = True
                return True

            seen.add(course)
            #path += f"->{course}"
            for prereq in prereqs[course]:
                if prereq in seen or not validate(prereq, set(seen)):
                    """
                    print("violation!")
                    print(f"path up to now: {path}")
                    print(f"prereqs of {course}: {prereqs[course]}")
                    print(f"seen: {seen}")
                    """
                    return False

            resolved[course] = True
            return True
        
        return all(validate(course, set()) for course in range(numCourses))
        