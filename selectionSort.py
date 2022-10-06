#User function Template for python3

class Solution: 
    
    
    def selectionSort( self,arr,n):
        self.arr =arr
        self.n = n
        for i in range(n):
            min = arr[i]
            for j in range(i+1,n):
                if min > arr[j]:

                    arr[i] = arr[j]
                    arr[j] = min
                    min = arr[i]
        return arr
    
    
