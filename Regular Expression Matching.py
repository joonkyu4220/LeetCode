class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        plen = len(p)
        pi = 0
        conditions = list()
        first = 0
        while pi < plen - 1:
            if p[pi+1] == "*":
                if first < pi:
                    conditions.append((p[first:pi], pi - first))
                conditions.append((p[pi], 0))
                pi += 2
                first = pi
            else:
                pi += 1
        if first < plen:
            conditions.append((p[first:plen], plen - first))
        
        def startable(s, condition):
            if condition[1]:
                if len(s) < condition[1]:
                    return 0
                for i in range(condition[1]):
                    if condition[0][i] == "." or condition[0][i] == s[i]:
                        continue
                    else:
                        return 0
                return condition[1]
            else:
                if condition[0][0] != ".":
                    for i in range(len(s)):
                        if s[i] != condition[0]:
                            return -(i+1)
                return -(len(s)+1)
            
        def recursive(s, conditions):
            check = startable(s, conditions[0])
            if (len(conditions) == 1):
                if (check and (len(s) == check or len(s) == -check - 1)):
                    return True
                else:
                    return False
            else:
                if check == 0:
                    return False
                elif check > 0:
                    return recursive(s[check:], conditions[1:])
                else:
                    ret = False
                    for i in range(-check):
                        ret = ret or recursive(s[i:], conditions[1:])
                    return ret
        
        return recursive(s, conditions)
