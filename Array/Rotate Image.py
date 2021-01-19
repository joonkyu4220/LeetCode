class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n % 2 == 0:
            m = 2
        else:
            m = 3
        
        while (len(matrix) - m) >= 0:
            cur = (n - m) / 2
            for j in range(m-1):
                matrix[cur + j][-1 - cur], matrix[-1 - cur][-1 - cur - j],\
                matrix[-1 - cur - j][cur], matrix[cur][cur + j]\
                = \
                matrix[cur][cur + j], matrix[cur + j][-1 - cur],\
                matrix[-1 - cur][-1 - cur - j], matrix[-1 - cur - j][cur]
            m += 2
                
            
            
