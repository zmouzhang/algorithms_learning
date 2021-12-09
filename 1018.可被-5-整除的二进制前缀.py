#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        pre = 0
        for i in nums:
            pre = ((pre<<1)+i)%5
            res.append(not pre)
        return res
# @lc code=end

