#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            # 恰好是末端节点，两个子节点都为空，那么它可以当场去世了
            # 只有一个非空子节点，那么它要让这个孩子接替自己的位置
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 获取右子树最小值
            minNode = self.getMin(root.right)
            # 删除右子树的最小值
            root.right = self.deleteNode(root.right, minNode.val)
            # 用右子树最小节点替代root节点
            # 在实际应用中，BST 节点内部的数据域是用户自定义的，
            # 可以非常复杂，而 BST 作为数据结构（一个工具人），
            # 其操作应该和内部存储的数据域解耦，
            # 所以我们更倾向于使用指针操作来交换节点，根本没必要关心内部数据
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

    # 获取二叉树搜索树最小值
    # 二叉搜索树最小值在最左边
    def getMin(self, root):
        while root.left:
            root = root.left
        return root
        
            
# @lc code=end

