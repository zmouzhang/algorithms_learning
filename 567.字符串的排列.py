#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 定义滑动窗口需要维护的数据， hashmap
        # hashmap_s1是固定值，不需要维护
        hashmap_s1, hashmap = {}, {}
        for char in s1:
            hashmap_s1[char] = hashmap_s1.get(char, 0) + 1
        # 定义滑动窗口的开始start
        start = 0
        for end in range(len(s2)):
            # 更新需要维护的数据hashmap
            hashmap[s2[end]] = hashmap.get(s2[end], 0) + 1
            if hashmap == hashmap_s1:
                return True
            # 此题的滑动窗口的大小其实就是s1字符串的长度。
            # 滑动窗口的大小不合法的情况，移动滑动窗口的左指针
            if end >= len(s1) - 1:
                head = s2[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        return False
# @lc code=end

