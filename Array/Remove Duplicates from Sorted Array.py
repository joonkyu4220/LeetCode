class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
		if len(nums) == 0:
            return 0;
        
        cur = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:
                nums[cur+1] = nums[i]
                cur += 1
                
        return cur + 1
