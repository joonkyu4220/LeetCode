# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if isBadVersion(1):
            return 1
        
        def recursiveHalf(start, end):
            if end - start <= 1:
                return end
            else:
                mid = (start + end)/2
                if isBadVersion(mid):
                    return recursiveHalf(start, mid)
                else:
                    return recursiveHalf(mid, end)
        
        return recursiveHalf(1, n)
