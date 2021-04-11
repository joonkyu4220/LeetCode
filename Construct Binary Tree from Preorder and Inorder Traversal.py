# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def __init__(self):
        self.order = {}
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        for i, io in enumerate(inorder):
            self.order[io] = i
                
        def build(preorder, pre_start, pre_end, inorder, ino_start, ino_end):
            if pre_start >= pre_end:
                return None
            idx = self.order[preorder[0]]
            l_len = idx-ino_start + 1
            l = build(preorder[1:l_len], pre_start+1, pre_start+l_len, inorder[:l_len-1], ino_start, idx)
            r = build(preorder[l_len:], pre_start+l_len, pre_end, inorder[l_len:], idx+1, ino_end)
            return TreeNode(val = preorder[0], left = l, right = r)
        
        return build(preorder, 0, len(preorder), inorder, 0, len(inorder))
            
#         p = preorder[0]
#         if len(preorder) == 1:
#             return TreeNode(p, None, None)
        
#         for i in range(len(inorder)):
#             if inorder[i] == p:
#                 l = self.buildTree(preorder[1:i+1], inorder[:i])
#                 r = self.buildTree(preorder[i+1:], inorder[i+1:])
#                 return TreeNode(p, left = l, right = r)
