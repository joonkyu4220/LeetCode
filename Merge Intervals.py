class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = [intervals[0]]
        
        for i in range(len(intervals)):
            l = intervals[i][0]
            r = intervals[i][1]
            lenAns = len(ans)
            start = 0
            end = 2 * lenAns
            
            for j in range(lenAns):
                if l > ans[j][1]:
                    start = 2 * j + 2
                elif l > ans[j][0]:
                    start = 2 * j + 1
                    break
            for j in range(lenAns-1, -1, -1):
                if r < ans[j][0]:
                    end = 2 * j
                elif r <= ans[j][1]:
                    end = 2 * j + 1
                    break
            if start < end:
                ans[start // 2][0] = min(l, ans[start // 2][0])
                if end % 2 == 0:
                    ans[start // 2][1] = r
                else:
                    ans[start // 2][1] = ans[end // 2][1]
                ans = ans[:start//2 + 1] + ans[(end+1)//2:]
            elif start%2 == 0:
                ans = ans[:start/2] + [[l, r]] + ans[start/2:]
        return ans
