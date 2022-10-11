class Solution(object):
    def dailyTemperatures(self, temperatures):
        self.temperatures = temperatures
        new_list = [0]*len(temperatures)
        

        for i in range(len(temperatures)):
            current = temperatures[i]
            max = temperatures[i]
            for k in range(i,len(temperatures)):
                if temperatures[k] > max:
                    max = temperatures[k]
            for j in range(i+1,len(temperatures)):
                if current == max:
                    
                    break
                elif current > temperatures[j] and current == temperatures[len(temperatures)-2]:
                    break
                elif current < temperatures[j]:
                    new_list[i] += 1
                    break
                else:
                    new_list[i] += 1
        return new_list
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
