# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        _len = len(nums)
        if _len == 0:
            return None
        elif _len == 1:
            return TreeNode(nums[0])
        else:
            return TreeNode(nums[_len/2], self.sortedArrayToBST(nums[:_len/2]), self.sortedArrayToBST(nums[_len/2 + 1:]))
