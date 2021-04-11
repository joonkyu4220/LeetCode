# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
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
        
        even = True
        for i in range(1, len(ret), 2):
            ret[i] = ret[i][::-1]
        
        return ret
