#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            tmp = str(x)
            target = ''
            for i in range(0, len(tmp)):
                target += tmp[len(tmp) -1 -i]
            if target == tmp:
                return True
            else:
                return False
# @lc code=

