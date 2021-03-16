class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # s = lower(s)
        # alphanum = 'qwertyuiopasdfghjklzxcvbnm0123456789'
        # i = 0
        # while(len(s) > i):
        #     if s[i] in alphanum:
        #         i += 1 
        #     else:
        #         s = s[:i] + s[i+1:]
        # if ''.join(reversed(s)) == s:
        #     return True
        # else:
        #     return False
        
        
        import re
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s).lower()
        return s == s[::-1]
