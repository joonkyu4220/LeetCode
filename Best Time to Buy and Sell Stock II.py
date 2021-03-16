class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        margin = 0
        
        for i in range(1, len(prices)):
            margin += max(0, prices[i] - prices[i-1])
            
        return margin
