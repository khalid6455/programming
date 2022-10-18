class Solution(object):
    def maxVowels(self, s, k):
        self.s = s
        self.k = k
        vowels = ['a','e','i','o','u']

        lst = []
        for i in range(len(s)-k+1):
            new_string = ''
            count = 0
            
            for j in range(k-1+1):
                new_string += s[i+j]
            for m in new_string:
                if m in vowels:
                    count+=1
            lst.append(count)
        lst.sort()
        return lst.pop()

        
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
