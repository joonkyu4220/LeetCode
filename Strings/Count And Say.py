class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        
        prev = self.countAndSay(n - 1)
        
        cur = ''
        
        new = 0
        repeat = 0
        
        for i in range(len(prev)):
            if prev[i] != new:
                cur += str(repeat)
                cur += str(new)
                new = prev[i]
                repeat = 1
            else:
                repeat += 1
        cur += str(repeat)
        cur += str(new)
            
        return cur[2:]
