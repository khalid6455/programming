class Solution(object):
    def moveZeroes(self, nums):
        self.nums = nums
        
       
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == 0:
                    temp = nums[j]
                    nums[j] = 0
                    nums[i] = temp
        
       
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
