# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        ret = [[root]]
        while True:
            ret.append([])
            for i in range(len(ret[-2])):
                head = ret[-2][i]
                if head.left:
                    ret[-1].append(head.left)
                if head.right:
                    ret[-1].append(head.right)
                ret[-2][i] = head.val
            if len(ret[-1]) == 0:
                ret.pop(-1)
                break
        
        return ret
