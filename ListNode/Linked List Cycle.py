# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
#         while (head):
#             if str(head.val) == head.val:
#                 return True
#             else:
#                 head.val = str(head.val)
#                 head = head.next
        
#         return False

        
        if not(head and head.next):
            return False
        fast = head.next
        slow = head
        while (fast.next and fast.next.next):
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False
            
