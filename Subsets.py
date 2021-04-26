class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_ = len(nums)
        ans = [[]]
        for n in nums:
            temp = []
            for a in ans:
                temp.append(a+[n])
            ans += temp
        return ans
