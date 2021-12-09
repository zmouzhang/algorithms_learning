#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先排序
        nums.sort()
        pivot = len(nums[::2])
        # 交叉替换
        nums[::2], nums[1::2] = nums[:pivot][::-1], nums[pivot:][::-1]
# @lc code=end

