class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row_max = len(matrix)
        
        row = 0
        col = len(matrix[0]) - 1
        
        while True:
            m = matrix[row][col]
            if m == target:
                return True
            if m < target:
                if row + 1 < row_max:
                    row += 1
                else:
                    return False
            elif m > target:
                if col > 0:
                    col -= 1
                else: return False
