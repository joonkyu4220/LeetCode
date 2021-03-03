class Solution(object):
    def divAndCon(self, nums, start, end):
        if start == end:
            return nums[start]
        mid = (start + end) // 2
        lmax = nums[mid]
        rmax = nums[mid+1]
        l = self.divAndCon(nums, start, mid)
        r = self.divAndCon(nums, mid+1, end)
        s = 0
        for i in range(mid, start-1, -1):
            s += nums[i]
            lmax = max(lmax, s)
        s = 0
        for i in range(mid+1, end+1):
            s += nums[i]
            rmax = max(rmax, s)
        return max(l, r, lmax + rmax)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curSum = 0
        maxSum = nums[0]
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum
        
        
        
        return self.divAndCon(nums, 0, len(nums)-1)        
