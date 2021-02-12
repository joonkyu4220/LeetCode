# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head = None
    def recursive(self, prev_, cur_):
        if not(cur_.next):
            self.head = cur_
            prev_.next.next = prev_
            prev_.next = None
        else:
            self.recursive(cur_, cur_.next)
            prev_.next.next = prev_
            prev_.next = None
    
    def reverseList(self, head):
        
        if (head == None or head.next == None):
            return head
        self.recursive(head, head.next)
        return self.head
        
        
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p
        
        # cur_ = head
        # prev_ = None
        # while (cur_):
        #     next_ = cur_.next
        #     cur_.next = prev_
        #     prev_ = cur_
        #     cur_ = next_
        # return prev_
        
        
            
