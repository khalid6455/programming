class Solution(object):
    def nextPermutation(self, nums):
        self.nums = nums
        for i in nums:
            min = nums[0]
            if i < min:
                min = i
        if ( min != nums[0]):
            if (nums[len(nums) - 2] > nums[len(nums) - 1]):
                nums.sort() 
        elif (nums[len(nums) - 2] < nums[len(nums) - 1]):
            temp = nums[len(nums) - 2]
            nums[len(nums) - 2] = nums[len(nums) - 1]
            nums[len(nums) - 1] = temp
        elif (min == nums[0]):
            if (nums[len(nums) - 2] < nums[len(nums) - 1]):
                temp = nums[len(nums) - 2]
                nums[len(nums) - 2] = nums[len(nums) - 1]
                nums[len(nums) - 1] = temp
            elif (nums[len(nums) - 2] > nums[len(nums) - 1]):
                temp = nums[len(nums) - 2]

                nums[len(nums) - 3] = nums[len(nums) - 1]
                nums[len(nums) - 2] = min
                nums[len(nums) - 1] = temp
        
       
        
        
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
