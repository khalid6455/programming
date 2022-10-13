class Solution(object):
    def rotate(self, nums, k):
        self.nums = nums
        self.k = k
        for i in range(k):
            temp = nums[len(nums)-1]
            nums.insert(0,temp)
            nums.pop()
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
