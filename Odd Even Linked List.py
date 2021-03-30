# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not(head):
            return head
        if not(head.next):
            return head
        
        odd = head
        even = head.next
        oddDummy = ListNode(None, odd)
        evenDummy = ListNode(None, even)
        while(odd and even):
            if even.next:
                odd.next = even.next
                odd = odd.next
            else:
                break
            if odd.next:
                even.next = odd.next
                even = even.next
            else:
                break
        even.next = None
        odd.next = evenDummy.next
        return oddDummy.next
        
