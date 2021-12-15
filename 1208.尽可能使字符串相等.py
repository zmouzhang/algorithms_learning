#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        sum_cost, max_len = 0, 0
        # 定义滑动窗口的开始
        start = 0
        for end in range(len(s)):
            sum_cost += abs(ord(s[end]) - ord(t[end]))
            if sum_cost <= maxCost:
                max_len = max(max_len, end-start+1)
            while sum_cost > maxCost:
                sum_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
        return max_len
# @lc code=end

