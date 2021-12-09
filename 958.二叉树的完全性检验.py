#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# /**
# 解题思路：
# 判断完全二叉树标准：
# 完全二叉树的节点为空时，后面应该没有节点。
# 步骤：
# 1，遍历所有的节点，并将节点加入到队列中，如果遇到空节点，则跳出循环；
# 2，遍历整个队列，如果节点为空，且后面的仍有不为空的节点，则判断为不是完全二叉树；
# **/
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        import collections
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node: 
                break
            q.append(node.left)
            q.append(node.right)
        for node in q:
            if node:
                return False
        return True
            
# @lc code=end

