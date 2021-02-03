class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        r = ""
        
        if not(len(strs)):
            return r
        
        
        strLens = [len(s) for s in strs]
        
        minLen = min(strLens)
        
        for i in range(minLen):
            strCrops = [s[i] for s in strs]
            if min(strCrops) == max(strCrops):
                r += strCrops[0]
            else:
                break
                
        return r
        
