class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_ = len(s)
        i = 0
        longest = 0

        
        while(i < len_):
            l = i
            r = i
            
            while(r < len_ and s[l] == s[r]):
                r += 1
            i = r
            r -= 1
            
            while(l >= 0 and r < len_ and s[l] == s[r]):
                l -= 1
                r += 1
            
            l += 1
            r -= 1
            
            
            
            if r - l + 1 > longest:
                longest = r - l + 1
                start = l
                
            
        return s[start:start + longest]
