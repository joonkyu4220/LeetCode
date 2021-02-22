# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

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
        
        maxi, mini = float('inf'), float('-inf')
        
        def traverse(root, maxi, mini):
            if root == None:
                return True
            l = traverse(root.left, root.val, mini)
            r = traverse(root.right, maxi, root.val)
            
            return l and r and (root.val > mini) and (root.val < maxi)
        
        return traverse(root, maxi, mini)
        
        
#         def maxVal(root):
#             if not(root):
#                 return (True, None)
#             elif not(root.left) and not(root.right):
#                 return (True, root.val)
#             elif not(root.left):
#                 rightMax = maxVal(root.right)
#                 if rightMax[0] and rightMax[1] > root.val:
#                     return (True, rightMax[1])
#                 else:
#                     return (False, None)
#             elif not(root.right):
#                 leftMax = maxVal(root.left)
#                 if leftMax[0] and leftMax[1] < root.val:
#                     return (True, root.val)
#                 else:
#                     return (False, None)
#             else:
#                 rightMax = maxVal(root.right)
#                 leftMax = maxVal(root.left)
#                 if rightMax[0] and leftMax[0] and leftMax[1] < root.val < rightMax[1]:
#                     return (True, rightMax[1])
#                 else:
#                     return (False, None)
    
#         def minVal(root):
#             if not(root):
#                 return (True, None)
#             elif not(root.left) and not(root.right):
#                 return (True, root.val)
#             elif not(root.left):
#                 rightMin = minVal(root.right)
#                 if rightMin[0] and rightMin[1] > root.val:
#                     return (True, root.val)
#                 else:
#                     return (False, None)
#             elif not(root.right):
#                 leftMin = minVal(root.left)
#                 if leftMin[0] and leftMin[1] < root.val:
#                     return (True, leftMin[1])
#                 else:
#                     return (False, None)
#             else:
#                 rightMin = minVal(root.right)
#                 leftMin = minVal(root.left)
#                 if rightMin[0] and leftMin[0] and leftMin[1] < root.val < rightMin[1]:
#                     return (True, leftMin[1])
#                 else:
#                     return (False, None)
                
#         if maxVal(root)[0] and minVal(root)[0]:
#             return True
#         else:
#             return False
