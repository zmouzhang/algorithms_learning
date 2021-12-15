#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 定义滑动窗口需要维护的数据
        res, hashmap = [], {}
        
        hashmap_p = {}
        for char in p:
            hashmap_p[char] = hashmap_p.get(char, 0) + 1
        start = 0
        for end in range(len(s)):
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            # 判断滑动窗口的
            if hashmap == hashmap_p:
                res.append(start)
            if end >= len(p) - 1:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
        return res        

            
# @lc code=end

