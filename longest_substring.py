class Solution(object):
    def lengthOfLongestSubstring(self, s):
        self.s = s
        s = list(s)
        lst = []
        for i in range(len(s)):

            temp = s[i]
    
            for j in  range(i+1,len(s)):
                if (s[j] in temp):
                    break
                if (s[j] not in temp):
                    temp += s[j]

            lst.append(len(temp))
        lst.sort()
        n = lst.pop()
        return n
        """
        :type s: str
        :rtype: int
        """
            
