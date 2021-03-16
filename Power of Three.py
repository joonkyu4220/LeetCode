class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n == 1:
        #     return True
        # elif n <= 0 or n % 3 != 0:
        #     return False
        # else:
        #     return self.isPowerOfThree(n / 3)
        
        if n <= 0:
            return False
        
        while True:
            if n == 1:
                return True
            elif n % 3:
                return False
            else:
                n /= 3
