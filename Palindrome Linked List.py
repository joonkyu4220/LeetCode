# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # mem = []
        # while (head):
        #     mem.append(head.val)
        #     head = head.next
        # return mem==mem[::-1]
        
        if not(head):
            return True
        
        fast = head
        slow = head
        while (fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        
        prev_ = None
        cur_ = slow.next
        while (cur_):
            next_ = cur_.next
            cur_.next = prev_
            prev_ = cur_
            cur_ = next_
        
        tail = prev_
        
        while (tail):
            if head.val != tail.val:
                return False
            else:
                tail = tail.next
                head = head.next
            
        return True
