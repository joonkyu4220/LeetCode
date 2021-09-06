class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        len_ = len(nums)
        result = [[0] * len_ for _ in range(len_)]
        for length in range(3, len_ + 1):
            for i in range(0, len_ - length + 1):
                j = i + length - 1
                for k in range(i + 1, j):
                    result[i][j] = max(result[i][k] + result[k][j] + nums[i] * nums[k] * nums[j], result[i][j])
        return result[0][len_ - 1]
