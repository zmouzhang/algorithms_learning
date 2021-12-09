#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s):
        dicmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        length = len(s)
        result = 0
        for i in range(0, length):
            if (i < length - 1) and (dicmap[s[i]] < dicmap[s[i+1]]):
                result -= dicmap[s[i]]
            else:
                result += dicmap[s[i]]
        return result 
        
# @lc code=end
