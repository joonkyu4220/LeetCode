class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        dic['I'] = 1
        dic['V'] = 5
        dic['X'] = 10
        dic['L'] = 50
        dic['C'] = 100
        dic['D'] = 500
        dic['M'] = 1000
        
        strLen = len(s)
        
        r = 0
        
        for i in range(strLen - 1):
            cur = dic[s[i]]
            nex = dic[s[i+1]]
            if cur < nex:
                r -= cur
            else:
                r += cur
            
        r += dic[s[-1]]
        
        return r
            
