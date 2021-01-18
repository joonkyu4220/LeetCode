class Solution(object):
    
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = -1
        
        while (i + len(digits) > -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1
        
        if digits[0] == 0:
            digits.insert(0, 1)
            return digits
