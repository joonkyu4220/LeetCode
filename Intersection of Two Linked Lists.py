# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummyA = ListNode(None, headA)
        dummyB = ListNode(None, headB)
        intersection = None
        
        while(headA):
            headA.val = -headA.val
            headA = headA.next
        while(headB):
            if headB.val < 0:
                intersection = headB
                break
            else:
                headB = headB.next
        headA = dummyA.next
        while(headA):
            headA.val = -headA.val
            headA = headA.next
        
        return intersection
