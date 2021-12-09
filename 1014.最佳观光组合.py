#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        pre_max = values[0] + 0
        for j in range(1,len(values)):
            res = max(res, pre_max+values[j]-j)
            pre_max = max(pre_max, values[j]+j)
        return res
# @lc code=end

