class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        curMax = 0
        for i in range(n):
            h = height[i]
            if h == 0:
                continue
            for j in range(i - curMax / h):
                if height[j] >= h:
                    curMax = (i - j) * h
                    break
            for j in range(n - 1, i + curMax/h, -1):
                if height[j] >= h:
                    curMax = (j - i) * h
                    break
        return curMax
