#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的满二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        res = []
        if n == 1:
            return [TreeNode(0)]
        # 满二叉树的节点个数不会是偶数
        if n %2 == 0:
            return []
        leftNum = 1
        rightNum = n - 2
        while rightNum > 0:
            # 递归构建左右子树
            left_tree = self.allPossibleFBT(leftNum)
            right_tree = self.allPossibleFBT(rightNum)
            for i in range(len(left_tree)):
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)
            leftNum += 2
            rightNum -= 2
        return res


# @lc code=end

