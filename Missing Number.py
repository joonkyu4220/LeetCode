class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_ = len(nums)
        s = len_ * (len_ + 1) / 2
        for n in nums:
            s -= n
        return s
