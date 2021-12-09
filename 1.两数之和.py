#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
# 思路：固定一个值，然后将差进行遍历。

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            otherNum = target - nums[i]
            if otherNum in nums:
                j = nums.index(otherNum)
                if i == j:
                    continue
                else:
                    return i, j
            else:
                continue
# @lc code=end

