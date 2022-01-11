#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBST_help(root, min=None, max=None)
    
    def isValidBST_help(self, root, min, max):
        if not root:
            return True
        if min != None and min.val >= root.val:
            return False
        if max != None and max.val <= root.val:
            return False
        return self.isValidBST_help(root.left, min, root) and self.isValidBST_help(root.right, root, max)
# @lc code=end

