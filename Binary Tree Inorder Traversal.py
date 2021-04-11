# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        heads = []
        vals = []
        cur = root
        
        while (cur is not None) or len(heads):
            if cur is None:
                back = heads[-1]
                vals.append(back.val)
                cur = back.right
                heads.pop()
            else:
                heads.append(cur)
                cur = cur.left
        return vals        
        
        
        if root is None:
            return []
        else:
            l = self.inorderTraversal(root.left)
            r = self.inorderTraversal(root.right)
            return l + [root.val] + r
