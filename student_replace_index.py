class Solution(object):
    def chalkReplacer(self, chalk, k):
        self.chalk = chalk 
        self.k = k
        count = 0
        while(chalk[count] <= k):
            k -= chalk[count]
            count += 1
            if count == len(chalk):
                count =0
        return count
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        
