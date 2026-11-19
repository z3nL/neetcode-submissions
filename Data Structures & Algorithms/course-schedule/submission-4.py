class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        def validate(course, seen):
            if course not in prereqs:
                return True

            for prereq in prereqs[course]:
                if prereq in seen or not validate(prereq, seen | {prereq}):
                    return False

            del prereqs[course]
            return True
        
        return all(validate(course, {course}) for course in range(numCourses))
        