#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 进行排序，按照第一个元素
        intervals.sort(key=lambda x:x[0])
        res = []
        for item in intervals:
            if not res or res[-1][1] < item[0]:
                res.append(item)
            else:
                res [-1][1] = max(res[-1][1], item[1])
        return res
# @lc code=end

