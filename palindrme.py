# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        self.head = head
        n = self.head
        new_list = []
        while n is not None:
            new_list.append(n)
        print(new_list)
        lst = []
        for i in range(len(new_list)-1,-1,-1):
            lst.append(new_list[i])
        return (lst == new_list)
        
        """
        :type head: ListNode
        :rtype: bool
        """
        
