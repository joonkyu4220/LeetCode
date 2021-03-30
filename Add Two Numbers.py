# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = ListNode()
        dummy = ListNode(None, cur)
        while(l1 and l2):
            cur.val += l1.val + l2.val
            cur.next = ListNode()
            if cur.val >= 10:
                cur.next.val = 1
                cur.val -= 10
            prev = cur
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            cur.val += l1.val
            cur.next = ListNode()
            if cur.val >= 10:
                cur.next.val = 1
                cur.val -= 10
            prev = cur
            cur = cur.next
            l1 = l1.next
        while(l2):
            cur.val += l2.val
            cur.next = ListNode()
            if cur.val >= 10:
                cur.next.val = 1
                cur.val -= 10
            prev = cur
            cur = cur.next
            l2 = l2.next
        if cur.val:
            cur.next = None
        else:
            prev.next = None
        return dummy.next
