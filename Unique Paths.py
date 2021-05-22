class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [1 for _ in range(n)]
        
        for i in range(1, m):
            for j in range(1, n):
                l[j] += l[j-1]
        return l[-1]
                
        
        # m, n = max(m, n), min(m, n)
        # mi = m-1
        # ni = n-1
        # ans = 1
        # while ni >= 1:
        #     ans *= (mi + ni)
        #     ans /= (n - ni)
        #     ni -= 1
        # return ans
