class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operatorList = ['+', '-', '*', '/']
        cur = ""
        
        nums = []
        ops = []
        
        cur = ""
        
        len_ = len(s)
        
        for i in range(len_):
            if s[i] in operatorList:
                nums.append(int(cur.replace(" ", "")))
                ops.append(s[i])
                cur = ""
            else:
                cur += s[i]
        nums.append(int(cur.replace(" ", "")))
        
        len_ = len(ops)
        i = 0
        while i < len_:
            if ops[i] == "*":
                nums[i] *= nums[i+1]
                nums = nums[:i+1] + nums[i+2:]
                ops = ops[:i] + ops[i+1:]
                len_ -= 1
            elif ops[i] == "/":
                nums[i] //= nums[i+1]
                nums = nums[:i+1] + nums[i+2:]
                ops = ops[:i] + ops[i+1:]
                len_ -= 1
            else:
                i += 1
        for i in range(len_):
            if ops[i] == "-":
                nums[i+1] *= -1
        
        return sum(nums)
