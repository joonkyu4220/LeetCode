class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        len_ = len(nums)
        if len_ == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len_-1
        
        for i in range(1, len_):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
