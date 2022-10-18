class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        self.arr = arr
        self.k = k
        self.threshold = threshold

        count = 0
        for i in range(len(arr)-k+1):
            new_list = []
            for j in range(k-1+1):
                new_list.append(arr[i+j])
            total = 0
            for m in new_list:
                total += m
            if total/k >= threshold:
                count+=1
        return count

        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        
