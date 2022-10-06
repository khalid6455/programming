class Solution(object):
    def sortSentence(self, s):
        self.s = s
       
        lst = s.split()
        new_list = [0]*len(lst)

        for i in lst:
            j = i[len(i)-1]
    
            new_list[int(j)-1] = i[:len(i)-1]
        
    
        result = ' '.join(new_list)
        return result
    
