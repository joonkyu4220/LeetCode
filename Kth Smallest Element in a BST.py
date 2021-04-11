# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        heads = []
        cur = root
        count = 0
        
        while (cur is not None) or len(heads):
            if cur is None:
                back = heads[-1]
                count += 1
                if count == k:
                    return back.val
                cur = back.right
                heads.pop()
            else:
                heads.append(cur)
                cur = cur.left
