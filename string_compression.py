class Solution(object):
    def compress(self, chars):
        self.chars = chars
        

        
        strs = ''
        for i in range(len(chars)-1):
            temp = chars[i]
            s = ''
            if temp != chars[i-1]:
                
                for j in range(i,len(chars)):
                    if (temp ==chars[j]):
                        s += chars[j]
            if (len(s) == 1):
                strs += temp
                
            elif(len(s) > 1 and len(s)< 10):
                strs += temp
                strs += str(len(s))
               
            elif(len(s) >= 10):
                strs += temp
                strs += str(len(s))
                
        chars = list(strs)
        return chars
        




        """
        :type chars: List[str]
        :rtype: int
        """
        
