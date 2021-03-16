class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        # Solution 1
        for i in range(len(s)/2):
          s[i], s[-i-1] = s[-i-1], s[i]
        
        # Solution 2
        s[:] = reversed(s[:])
        
        # Solution 3
        s.reverse()
