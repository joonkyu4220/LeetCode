class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        cur = [[nums[0]]]
        for i in range(1, len(nums)):
            prev = cur
            cur = [(c[:j] + [nums[i]] + c[j:]) for j in range(i+1) for c in cur]
        
        return cur
