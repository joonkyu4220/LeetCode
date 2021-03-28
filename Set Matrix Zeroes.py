class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        numRow = len(matrix)
        numCol = len(matrix[0])
        
        firstRow = False
        firstCol = False
        
        for i in range(numRow):
            if matrix[i][0] == 0:
                firstCol = True
                break
        for j in range(numCol):
            if matrix[0][j] == 0:
                firstRow = True
                break
        
        for i in range(numRow):
            for j in range(numCol):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
                    
        
        for i in range(1, numRow):
            if matrix[i][0] == 0:
                for j in range(1, numCol):
                    matrix[i][j] = 0
        for j in range(1, numCol):
            if matrix[0][j] == 0:
                for i in range(1, numRow):
                    matrix[i][j] = 0
        
        if firstRow:
            for j in range(numCol):
                matrix[0][j] = 0
        if firstCol:
            for i in range(numRow):
                matrix[i][0] = 0
        
        
