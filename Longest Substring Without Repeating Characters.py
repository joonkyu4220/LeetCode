class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        dic = {}
        
        curInit = 0
        curLen = 0
        maxLen = 0
        
        for i in range(len(s)):
            c = s[i]
            if c in dic:
                if dic[c] >= curInit:
                    curLen -= (dic[c] + 1 - curInit)
                    curInit = dic[c] + 1
            curLen += 1
            dic[c] = i
            
            maxLen = max(maxLen, curLen)
            
        
        return maxLen
