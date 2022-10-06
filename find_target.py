class Solution(object):
    def targetIndices(self, nums, target):
        self.nums = nums
        self.target = target
        nums.sort()
        newlist_target =[]
        if target in nums:
            
            for i in range(len(nums)):
                if target== nums[i]:
                    newlist_target.append(i)
            return newlist_target
        else:
            return newlist_target
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
