# Definition for singly-linked list.
#class ListNode(object):
 #   def __init__(self, val=0, next=None):
  #      self.val = val
   #     self.next = next
class Solution(object):
    def middleNode(self, head = None):
        self.head = head
        count = 0
        n = self.head
        while n is not None:
            count += 1
            n = n.next
        
        size = count //2
        current = self.head
        for i in range(size):
            current = current.next
        return current
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
