class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        unvisitedCount = len(isConnected)
        unvisited = [i for i in range(unvisitedCount)]
        sccCount = 0
        while unvisitedCount:
            cur = list()
            sccCount += 1
            cur.append(unvisited[0])
            unvisited.pop(0)
            curCount = 1
            unvisitedCount -= 1
            i = 0
            while (i < curCount):
                x = cur[i]
                j = 0
                while j < unvisitedCount:
                    y = unvisited[j]
                    if isConnected[x][y]:
                        for c in cur:
                            isConnected[c][y] = 0
                            isConnected[y][c] = 0
                        cur.append(y)
                        curCount += 1
                        unvisited.pop(j)
                        unvisitedCount -= 1
                    else:
                        j += 1
                i += 1
        return sccCount
