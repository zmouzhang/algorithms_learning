#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x):
        if (-2 ** 31 <= x <= 2**31 - 1) and (x != 0):
            tmp = ''
            s = str(x)
            if x > 0:
                for i in range(0, len(s)):
                    tmp += s[len(s) - 1 - i]
            elif x < 0:
                tmp = '-'
                for i in range(1, len(s)):
                    tmp += s[len(s) - i]
            target = int(tmp)
            return target if -2 ** 31 <= target <= 2 ** 31 - 1 else 0
        else:
            return 0
            
# @lc code=end

