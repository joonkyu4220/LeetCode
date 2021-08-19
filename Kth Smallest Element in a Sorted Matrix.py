class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def putInSortedList(sortedList, newVal):
            if len(sortedList) == 0:
                return [newVal]
            nv = newVal[0]
            if nv <= sortedList[0][0]:
                return [newVal] + sortedList
            elif nv >= sortedList[-1][0]:
                return sortedList + [newVal]
            l = 0
            r = len(sortedList) - 1
            m = (l + r) / 2
            
            while (l < m):
                if sortedList[m][0] <= nv:
                    l = m
                else:
                    r = m
                m = (l + r) / 2
            return sortedList[:l+1] + [newVal] + sortedList[l+1:]
        len_ = len(matrix)
        conditions = [[2 for i in range(len_)] for j in range(len_)]
        for i in range(1, len_):
            conditions[i][0] = 1
            conditions[0][i] = 1
        conditions[0][0] = 0
        sortedList = [(matrix[0][0], 0, 0)]
        while True:
            k -= 1
            if k == 0:
                return sortedList[0][0]
            i = sortedList[0][1]
            j = sortedList[0][2]
            sortedList = sortedList[1:]
            if (i + 1) < len_:
                conditions[i+1][j] -= 1
                if conditions[i+1][j] == 0:
                    sortedList = putInSortedList(sortedList, (matrix[i+1][j], i+1, j))
            if (j + 1) < len_:
                conditions[i][j+1] -= 1
                if conditions[i][j+1] == 0:
                    sortedList = putInSortedList(sortedList, (matrix[i][j+1], i, j+1))
