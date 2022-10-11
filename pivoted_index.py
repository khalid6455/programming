class Solution(object):
    def pivotIndex(self, nums):
        self.nums = nums
      
        result = None
        for i in range(len(nums)):
            left_sum = 0
            rigth_sum =0
            for k in range(0,i):
                left_sum += nums[k]
            for m in range(i+1,len(nums)):
                rigth_sum += nums[m]
            if left_sum == rigth_sum:
                result = i
                break

        if result is None:
            return -1
        elif result != None:
            return result
            """
            :type nums: List[int]
            :rtype: int
            """
