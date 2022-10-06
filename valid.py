class Solution(object):
    def isValid(self, s):
        self.s = s
        for i in range(len(s)-1):
            if s[ i ] == s[ i+1 ]:
                result = 'true' 
            else:
                result = 'false'
            
        return result    
        """
        :type s: str
        :rtype: bool
        """
        
