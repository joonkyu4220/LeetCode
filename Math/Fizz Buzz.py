class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        ret = list()
        
        for i in range(1, n+1):
            s = ""
            if not(i % 3):
                s += "Fizz"
            if not(i % 5):
                s += "Buzz"
            if len(s):
                ret.append(s)
            else:
                ret.append(str(i))
        
        return ret
            
