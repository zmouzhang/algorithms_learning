#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
import math
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        TODO: 利用滑动窗口进行解题
        """
        # 定义滑动窗口需要维护的变量
        max_len, hashmap = 0, {}
        # 定义滑动窗口开始
        start = 0
        for end in range(len(nums)):
            item = nums[end]
            hashmap[item] = hashmap.get(item, 0) + 1
            if hashmap.get(0, 0) <=k:
                max_len = max(max_len, end-start+1)
            while hashmap.get(0,0) > k:
                head = nums[start]
                hashmap[head] -= 1
                start += 1
        return max_len
# @lc code=end

