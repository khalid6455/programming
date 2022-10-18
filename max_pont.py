class Solution(object):
    def maxScore(self, cardPoints, k):
        self.cardPoints = cardPoints
        self.k = k
        sum = 0
        for i in range(k-1+1):
            if cardPoints[0] > cardPoints[len(cardPoints)-1]:
                sum += cardPoints[0]
                cardPoints.pop(0)
            elif(cardPoints[len(cardPoints)-1] >= cardPoints[0]):
                sum += cardPoints[len(cardPoints)-1]
                cardPoints.pop()
                
        return sum
        
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
