class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.min) == 0 or self.min[-1]>x:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) == 0:
            return None
        else:
            self.stack = self.stack[:-1]
            self.min = self.min[:-1]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
