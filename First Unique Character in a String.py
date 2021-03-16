class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
#         dic = []
#         for i in range(len(s)):
#             if s[i] in dic:
#                 continue
#             else:
#                 for j in range(i+1, len(s)):
#                     if s[j] == s[i]:
#                         dic.append(s[i])
#                         break
#                 if s[i] in dic:
#                     continue
#                 else:
#                     return i
#         return -1
        
        dic = {}
        for c in s:
            if not(c in dic):
                dic[c] = 1
            else:
                dic[c] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
                             
