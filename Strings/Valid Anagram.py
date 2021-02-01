class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False

        # if set(s) == set(t):
        #     for c in s:
        #         if s.count(c) != t.count(c):
        #             return False
        #     return True
        # else:
        #     return False
                
                
        # if len(s) > len(t):
        #     for c in set(s):
        #         if s.count(c) != t.count(c):
        #             return False
        #     return True
        # else:
        #     for c in set(t):
        #         if s.count(c) != t.count(c):
        #             return False
        #     return True
