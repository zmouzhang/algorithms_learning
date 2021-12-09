#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#

# @lc code=start
"""
利用排序以及最小堆来进解题
1，先将数据集进行排序，按照上车时间进行排序即（x[1]）
2，利用最小堆的特性-出堆都是最小的元素，将上一个目的地（x[2]）与下一个出发地（x[1]）进行比较
3，如果小于下一个的出发第，则进行“下车操作”（while循环），车里面的座位数进行增加
4，如过车的座位数不够，就返回失败，即False

"""
import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        dist = []
        heapq.heapify(dist)
        for i in range(len(trips)):
            # 下一站的目的地大于等于之前一站的
            while dist and dist[0][0] <= trips[i][1]:
                end, passengers = heapq.heappop(dist)
                capacity += passengers
            if capacity < trips[i][0]:
                return False
            capacity -= trips[i][0]
            heapq.heappush(dist, [trips[i][2], trips[i][0]])
        return True
# @lc code=end

