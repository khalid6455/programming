class Solution(object):
    def numberOfSubarrays(self, nums, k):
        self.nums = nums
        self.k = k
        count = 0
        for i in range(len(nums)):
            result = 0
            for j in range(i,len(nums)):
                if (nums[j] % 2 != 0):
                    result += 1
                if (result == k):
                    count += 1
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
