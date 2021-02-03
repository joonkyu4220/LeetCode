class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        hayLen = len(haystack)
        neeLen = len(needle)
        
        if neeLen == 0:
            return 0;
        
        if neeLen > hayLen:
            return -1
        
        for i in range(hayLen - neeLen + 1):
            if haystack[i:i+neeLen] == needle:
                return i
        
        return -1
            
            
