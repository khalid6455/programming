class Solution(object):
    def productExceptSelf(self, nums):
        self.nums = nums
      
        lst =[]
        for i in range(len(nums)):
            p1 = 1
            p2 = 1
            for j in  range(0,i):
                p1 *= nums[j]
            for k in range(i+1,len(nums)):
                p2 *= nums[k]
            lst.append(p1*p2)
            p1 = 1
            p2 = 1
        return lst
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
