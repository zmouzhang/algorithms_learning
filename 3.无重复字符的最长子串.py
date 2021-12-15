#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 一，定义要维护的变量，本题求得是最大长度，所以max_len
        # 同时有涉及到去重，可以采用hasmap来实现去重
        max_len, hashmap = 0, {}
        # 二，定义窗口得首尾段（start, end）,然后滑动窗口
        
        start = 0
        for end in range(len(s)):
            # 三，将元素加入到hashmap里面，并更新最大长度
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if len(hashmap) == end - start + 1:
                max_len = max(max_len, end-start+1)
        # 四，根据题意，窗口得大小是可变：这个时候一般涉及窗口合不合法得问题
        # 这个时候需要用while去移动窗口得左指针，从而剔除非法元素，从而使窗口合法
        # 当窗口长度大于哈希表长度得时候（说明有重复元素），窗口不合法
        # 所以不断移动窗口得左指针直到窗口再次合法，同时也需要维护变量（hashmap）
            while end - start + 1 > len(hashmap):
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        # 五，返回答案（最大长度）
        return max_len

# @lc code=end

