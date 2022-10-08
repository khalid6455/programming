class MinStack(object):

    def __init__(self):
        self.arg =[]
        

    def push(self, val):
        self.arg.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.arg.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.arg[-1]
        
        """
        :rtype: int
        """
        

    def getMin(self):
        minm = self.arg[0]
        for i in self.arg:
            if i < minm :
                minm = i
        return minm   
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
