class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        cur = 2
        i = 2
        while i < n-1:
            prev, cur = cur, prev+cur
            i += 1
        return prev + cur
