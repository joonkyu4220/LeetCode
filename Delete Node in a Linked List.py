class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
#         while(node.next.next):
#             node.val = node.next.val
#             node = node.next
        
#         node.val = node.next.val
#         node.next = None
