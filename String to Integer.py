class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        ans = 0
        i = 0
        
        while(i < len(s)):
            if s[i].isdigit():
                break
            elif s[i] == '-':
                sign *= -1
                i += 1
                break
            elif s[i] == '+':
                i += 1
                break
            elif s[i] == ' ':
                i += 1
            else:
                break
        
        while(i < len(s)):
            if s[i].isdigit():
                ans = 10 * ans + int(s[i])
                i += 1
            else:
                break
        
        ans *= sign
        
        if -2147483648 <= ans < 2147483648:
            return ans
        elif ans < -2147483648:
            return -2147483648
        else:
            return 2147483647
