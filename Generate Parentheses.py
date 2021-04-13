class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        cur = ['(']
        
        def counter(s):
            l = 0
            r = 0
            for c in s:
                if c == '(':
                    l += 1
                else:
                    r += 1
            return (l, r)
        
        for _ in range(n * 2 - 1):
            prev = cur
            cur = []
            for p in prev:
                (l, r) = counter(p)
                if l==r:
                    cur.append(p+'(')
                elif l==n:
                    cur.append(p+')')
                else:
                    cur.append(p+')')
                    cur.append(p+'(')
        return cur
