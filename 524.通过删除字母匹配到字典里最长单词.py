#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def isSubsquence(self, s:str, t:str)->bool:
        n, m = len(s), len(t)
        if m > n: return False
        i = 0
        for ch in t:
            while i < n and s[i] != ch:
                i += 1
            if i >= n:
                return False
            i += 1
        return True
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x), x))
        for word in dictionary:
            if self.isSubsquence(s, word):
                return word 
        return ''
# @lc code=end

