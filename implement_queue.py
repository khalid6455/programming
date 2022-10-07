class MyQueue(object):
    

    
    def __init__(self):
        self.lst = []
        

    def push(self, x ):
        self.lst.append(x)
        
       
        

    def pop(self):
        return self.lst.pop(0)
        
        

    def peek(self):
        return self.lst[0]
       

    def empty(self) :
        return len(self.lst) == 0
       
