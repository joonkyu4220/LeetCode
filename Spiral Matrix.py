class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        i = 0
        j = 0
        
        rowUpper = len(matrix) - 1
        rowLower = 0
        colUpper = len(matrix[0]) - 1
        colLower = 0
        answer = []
        
        while (rowUpper >= rowLower) and (colUpper >= colLower):
            while j <= colUpper:
                answer.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1
            rowLower += 1
            if rowLower > rowUpper:
                break
            
            while i <= rowUpper:
                answer.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            colUpper -= 1
            if colLower > colUpper:
                break

            while j >= colLower:
                answer.append(matrix[i][j])
                j -= 1
            j += 1
            i -= 1
            rowUpper -= 1
            if rowLower > rowUpper:
                break
            
            while i >= rowLower:
                answer.append(matrix[i][j])
                i -= 1
            i += 1
            j += 1
            colLower += 1
            if colLower > colUpper:
                break
        return answer
            
            
