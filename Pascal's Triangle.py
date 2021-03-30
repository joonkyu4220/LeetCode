class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        elif numRows < 2:
            return [[1]]
        
        r = [[1]]
        for i in range(2, numRows + 1):
            temp = []
            temp.append(1)
            for j in range(1, i - 1):
                temp.append(sum(r[-1][j-1:j+1]))
            temp.append(1)
            r.append(temp)
        return r
