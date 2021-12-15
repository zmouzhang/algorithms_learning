#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
#

# @lc code=start
import math
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        TODO: 该题求得是首尾串最大值，其实求得是非首尾串得最小值
        可以将固定得K滑动窗口转变成 len(cardPoints) - k 得滑动窗口最小值
        """
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        sum_, min_sum, m = 0, math.inf, n-k
        start = 0
        for end in range(len(cardPoints)):
            sum_ += cardPoints[end]
            if end >= m-1:
                min_sum = min(sum_, min_sum)
                sum_ -= cardPoints[start]
                start += 1
        return sum(cardPoints) - min_sum

# @lc code=end

