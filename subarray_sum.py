class Solution(object):
    def subarraySum(self, nums, k):
        self.nums = nums
        self.k = k
      
        count =0
       
        for i in range(len(nums)):
            sum = 0
            
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
                    sum = 0
                    break
            
       
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
