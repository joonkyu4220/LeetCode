class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        l = [0]
        coins.sort()
        for a in range(1, amount + 1):
            temp = [10001]
            for c in coins:
                if c <= a:
                    temp.append(l[a-c] + 1)
                else:
                    break
            l.append(min(temp))
        if l[-1] < 10001:
            return l[-1]
        else:
            return -1
