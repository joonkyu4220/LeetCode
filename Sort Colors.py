class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0, 0]
        for n in nums:
            count[n] += 1
        sum_ = 0
        for i in range(3):
            for j in range(sum_, sum_+count[i]):
                nums[j] = i
            sum_ += count[i]
