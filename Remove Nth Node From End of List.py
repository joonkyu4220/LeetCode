# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        
        head = ListNode(None, head)
        cur = head
        mem = list()
        
        idx = 0
        
        for i in range(n):
            mem.append(cur)
            cur = cur.next
        
        while (cur.next):
            mem[idx] = cur
            cur = cur.next
            idx = (idx + 1) % n
        
        mem[idx].next = mem[idx].next.next
        
        return head.next
        
        
#         cur = head
#         sz = 1
#         while (cur.next):
#             cur = cur.next
#             sz += 1
#         cur = head
#         if sz == n:
#             return head.next
#         for i in range(sz):
#             if i == sz-n-1:
#                 cur.next = cur.next.next
#                 return head
#             else:
#                 cur = cur.next
                
#         cur = head
#         sz = 1
#         while(cur.next):
#             cur = cur.next
#             sz += 1
#         head = ListNode(None, head)
#         cur = head
#         for i in range(sz):
#             if i == sz - n:
#                 cur.next = cur.next.next
#                 return head.next
#             else:
#                 cur = cur.next

        
