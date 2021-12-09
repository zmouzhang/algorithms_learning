#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, strs):
        if int(len(strs) % 2) != 0:
            return False
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for item in strs:
            if item in dic:
                stack.append(item)
            elif stack and dic[stack[-1]] == item:
                del stack[-1]
            else:
                return False
        return not stack
            
# @lc code=end

