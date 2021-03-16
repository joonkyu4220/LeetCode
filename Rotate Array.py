class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k %= len(nums)
        
        if k:
            start = 0
            end = len(nums)
            reverse = False
            while(end - start > k):
                if 2 * k > (end - start):
                    k = end - start - k
                    reverse = not(reverse)
                if not(reverse):
                    for i in range(k):
                        nums[start + i], nums[end - k + i] = nums[end - k + i], nums[start + i]
                    start += k
                else:
                    for i in range(1, k+1):
                        nums[end-i], nums[start+k-i] = nums[start+k-i], nums[end-i]
                    end -= k
