class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preReqs = defaultdict(int)
        nextCourse = defaultdict(list)

        for prereq in prerequisites: 
            preReqs[prereq[0]] += 1
            nextCourse[prereq[1]].append(prereq[0])
        
        stack = []
        visited = 0
        for i in range(numCourses):
            if preReqs[i] == 0:
                stack.append(i)
                visited += 1

        while stack:
            course = stack.pop()
            for nCourse in nextCourse[course]:
                if preReqs[nCourse] > 0:
                    preReqs[nCourse] -= 1
                    if preReqs[nCourse] == 0:
                        stack.append(nCourse)
                        visited += 1
        
        return visited == numCourses
        
