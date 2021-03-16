class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        
        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] = True
        
        return False
