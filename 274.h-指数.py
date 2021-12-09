#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse =True)
        h, i, n = 0, 0, len(citations)
        while i< n and citations[i] > h:
            h += 1
            i += 1
        return h
# @lc code=end
