class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True for _ in range(n)]
                
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        
        count = 0
        
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        
        return count
