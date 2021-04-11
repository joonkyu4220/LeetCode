"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        root.next = None
        dummy = Node(0, left=None, right=None, next=root)
        cur = root
        first = cur
        while cur is not None:
            first = cur
            if first.left is not None:
                while cur.next is not None:
                    cur.left.next = cur.right
                    cur.right.next = cur.next.left
                    cur = cur.next
                cur.left.next = cur.right
                cur.right.next = None
                cur = first.left
                continue
            else:
                break
                    
        return dummy.next
