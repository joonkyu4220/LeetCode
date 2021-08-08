class Solution(object):
    
    def __init__(self):
        self.max = 0
    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        numRow = len(matrix)
        numCol = len(matrix[0])
        visited = [[0 for _ in range(numCol)] for _ in range(numRow)]
        def startFrom(i, j):
            if visited[i][j]:
                return visited[i][j]
            visited[i][j] = 1
            if (0 <= (i+1) < numRow):
                if matrix[i+1][j] > matrix[i][j]:
                    visited[i][j] = max(startFrom(i+1, j) + 1, visited[i][j])
            if (0 <= (i-1) < numRow):
                if matrix[i-1][j] > matrix[i][j]:
                    visited[i][j] = max(startFrom(i-1, j) + 1, visited[i][j])
            if (0 <= (j+1) < numCol):
                if matrix[i][j+1] > matrix[i][j]:
                    visited[i][j] = max(startFrom(i, j+1) + 1, visited[i][j])
            if (0 <= (j-1) < numCol):
                if matrix[i][j-1] > matrix[i][j]:
                    visited[i][j] = max(startFrom(i, j-1) + 1, visited[i][j])
            return visited[i][j]        
                
        curMax = 0
        for i in range(numRow):
            for j in range(numCol):
                if visited[i][j] == 0:
                    startFrom(i, j)
                curMax = max(curMax, visited[i][j])
        return curMax
