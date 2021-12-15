#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        TODO: 利用滑动窗口进行解题,
            利用滑动窗口可以计算到挽留顾客最大数，与原本不生气的时间的顾客总数相加
        """
        # 定义滑动窗口要维护的变量，总收入，以及知道老板发动技能的最佳时间 max_start
        sum_, max_sum = 0, 0
        start = 0 
        for end in range(len(grumpy)):
            if grumpy[end]:
                sum_ += customers[end]
            # 更新需要维护的变量 (sum_)
            # 注意：这里只要当老板在当前时间点会发脾气的时候才维护
            # sum_就不说了，和前面N道题的维护方法一样，新多出来的max_start也就是记录一样时间点而已
            if sum_ > max_sum:
                max_sum = sum_
            # 根据题意可知窗口长度固定 (老板技能持续时间固定)，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (sum_)
            # 发动技能，这样生气赶走的顾客数就减少对应的人数（customer[start]）
            if end >= minutes - 1:
                if grumpy[start]:
                    sum_ -= customers[start]
                start += 1
        # 这里对比其他题目多了一小步: 在找到老板发动技能的最大收益时间点(max_start)后
        # 需要把受技能影响时间段中的grumpy全部置0 - 代表老板成功压制了自己的怒火
        res = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                res += customers[i]
        return res + max_sum

            


# @lc code=end

