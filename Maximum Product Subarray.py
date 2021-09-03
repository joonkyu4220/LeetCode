class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        posMax = 0
        negMax = 0
        curMax = nums[0]
        len_ = len(nums)
        for n in nums:
            if n > 0:
                if posMax:
                    posMax *= n
                else:
                    posMax = n
                negMax *= n
            elif n < 0:
                if posMax:
                    posMax, negMax = negMax * n, posMax * n
                else:
                    posMax, negMax = negMax * n, n
            else:
                posMax = 0
                negMax = 0
            curMax = max(curMax, posMax)
        return curMax
