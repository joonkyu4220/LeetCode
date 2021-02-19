# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not(root):
            return True
        elif not(root.left) and not(root.right):
            return True
        else:
            leftMax = self.maxVal(root.left)
            rightMin = self.minVal(root.right)
            
            if self.isValidBST(root.left) and self.isValidBST(root.right):
                
                if leftMax is not None:
                    if leftMax < root.val:
                        if rightMin is not None:
                            if root.val < rightMin:
                                return True
                            else:
                                return False
                        else:
                            return True
                    else:
                        return False
                            
                else:
                    if rightMin is not None:
                        if root.val < rightMin:
                            return True
                        else:
                            return False
            else:
                return False
            
    
    def maxVal(self, root):
        if not(root):
            return None
        elif not(root.left) and not(root.right):
            return root.val
        elif not(root.left):
            return max(root.val, self.maxVal(root.right))
        elif not(root.right):
            return max(root.val, self.maxVal(root.left))
        else:
            return max(root.val, self.maxVal(root.left), self.maxVal(root.right))
    
    def minVal(self, root):
        if not(root):
            return None
        elif not(root.left) and not(root.right):
            return root.val
        elif not(root.left):
            return min(root.val, self.minVal(root.right))
        elif not(root.right):
            return min(root.val, self.minVal(root.left))
        else:
            return min(root.val, self.minVal(root.left), self.minVal(root.right))
