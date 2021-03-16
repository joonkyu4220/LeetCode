# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not(root):
            return True
        toyTree = TreeNode(0, None, None)
        cur = [root]
        
        while True:
            prev = cur
            cur = []
            for i in range(len(prev)):
                head = prev[i]
                cur.append(head.left)
                cur.append(head.right)
            test = []
            found = False
            i = 0 
            while i < len(cur):
                if cur[i]:
                    test.append(cur[i].val)
                    i += 1
                else:
                    test.append(101)
                    cur.pop(i)
            if len(cur) == 0:
                return True
            
            if test != test[::-1]:
                return False
