class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        self.nums = nums
        n = len(nums)
        new_list = [0]*n
        for i in range(n):
            current_num = nums[i]
            for j in range(n):
                if(current_num > nums[j]):
                    new_list[i] += 1
        return new_list
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
