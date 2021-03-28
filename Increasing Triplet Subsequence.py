class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = 2147483647, 2147483647
        
        for n in nums:
            if first >= n:
                first = n
            elif second >= n:
                second = n
            else:
                return True
            
        return False
