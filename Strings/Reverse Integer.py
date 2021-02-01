class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        
        s = str(x)
        l = list(s)
        l.reverse()
        
        r = int(''.join(l))
        
        if -2 ** 31  <= r < 2 ** 31:
            return sign * r
        else:
             return 0
            
        
        
#         sign = [1, -1][x < 0]
#         s = sign * int(str(sign * x)[::-1])
        
#         if -2 ** 31 <= s < 2 ** 31:
#             return s
#         else:
#             return 0
