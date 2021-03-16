class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curmin = prices[0]
        profit = 0
        for p in prices:
            profit = max(p - curmin, profit)
            curmin = min(curmin, p)
        return profit
