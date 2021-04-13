class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        ans = ['']
        dic = {}
        dic['2'] = ['a', 'b', 'c']
        dic['3'] = ['d', 'e', 'f']
        dic['4'] = ['g', 'h', 'i']
        dic['5'] = ['j', 'k', 'l']
        dic['6'] = ['m', 'n', 'o']
        dic['7'] = ['p', 'q', 'r', 's']
        dic['8'] = ['t', 'u', 'v']
        dic['9'] = ['w', 'x', 'y', 'z']
        for d in digits:
            options = dic[d]
            ans = [a+o for a in ans for o in options]
        return ans
