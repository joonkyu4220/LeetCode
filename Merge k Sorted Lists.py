# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwo(l1, l2):
            dummy = ListNode(None, None)
            cur = dummy
            while ((l1 is not None) and (l2 is not None)):
                if l1.val < l2.val:
                    cur.next = l1
                    cur = cur.next
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = cur.next
                    l2 = l2.next
            if l1 is None:
                cur.next = l2
                return dummy.next
            elif l2 is None:
                cur.next = l1
                return dummy.next
        
        sortedList = None
        for listnode in lists:
            sortedList = mergeTwo(sortedList, listnode)
        
        return sortedList
