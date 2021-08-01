class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # import numpy as np
        # A = np.zeros((numCourses, numCourses))
        # for p in prerequisites:
        #     A[p[0]][p[1]] = 1
        # W, _ = np.linalg.eig(A)
        # if sum(W) == 0:
        #     return True
        # else: return False
        
        taken = []
        
        A = [[0 for j in range(numCourses)] for i in range(numCourses)]
        for p in prerequisites:
            A[p[0]][p[1]] = 1
        numPrerequisites = [sum(A[i]) for i in range(numCourses)]
        
        taken = list()
        for i in range(numCourses):
            if numPrerequisites[i] == 0:
                taken.append(i)
        
        idx = 0
        while (idx < len(taken) < numCourses):
            cur = taken[idx]
            for j in range(numCourses):
                if A[j][cur]:
                    A[j][cur] = 0
                    numPrerequisites[j] -= 1
                    if numPrerequisites[j] == 0:
                        taken.append(j)
            idx += 1
        if len(taken) == numCourses:
            return True
        else:
            return False
