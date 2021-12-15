#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 一， 定义需要维护的变量, 平均值以及k个数的和
        import math
        avgNum, total = -math.inf, 0
        # 二，定义滑动窗口
        start = 0
        # 遍历数组
        for end in range(len(nums)):
            total += nums[end]
            # 三，将窗口内的元素进行加和，并区别平均值，维护最开始的变量（平均值、总和）
            if end - start + 1 == k:
                avgNum = max(avgNum, total/k)
            # 该题的题意可以直到，窗口的大小是固定的，所以采用if condition
            # 窗口首指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (total)
            if end >= k - 1:
                total -= nums[start]
                start += 1
        return avgNum


# @lc code=end

