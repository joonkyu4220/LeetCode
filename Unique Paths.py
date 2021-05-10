class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m, n = max(m, n), min(m, n)
        mi = m-1
        ni = n-1
        ans = 1
        while ni >= 1:
            ans *= (mi + ni)
            ans /= (n - ni)
            ni -= 1
        return ans
