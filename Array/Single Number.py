class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        r = 0
        
        for n in nums:
            r = r ^ n
        
        return r
            
