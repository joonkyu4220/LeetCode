class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur = 0
        nonzero = 0
        
        while nonzero < len(nums):
            if nums[nonzero] != 0:
                nums[cur], nums[nonzero] = nums[nonzero], nums[cur]
                cur += 1
            nonzero += 1
