class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        r = [-10001 for _ in range(k)]
        
        for n in nums:
            for i in range(k):
                if r[i] < n:
                    r[i+1:] = r[i:-1]
                    r[i] = n 
                    break
        return r[k-1]
