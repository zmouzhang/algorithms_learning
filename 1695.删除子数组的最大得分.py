#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#

# @lc code=start
import math
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        sum_, hashmap, max_sum = 0, {}, -math.inf
        #定义滑动窗口的开始与结束
        start = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            hashmap[nums[end]] = hashmap.get(nums[end], 0) + 1
            if end - start + 1 == len(hashmap):
                max_sum = max(max_sum, sum_)
            # 当滑动窗口大于hashmap长度，说明有重复的值
            while end-start+1 > len(hashmap):
                head = nums[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]    
                sum_ -= nums[start]
                start += 1
        return max_sum
# @lc code=end

