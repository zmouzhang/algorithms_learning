#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        i, j, cnt, sumCnt, res = 0, 0, 0, 0, 0
        while j < len(customers):
            if grumpy[j] == 0:
                sumCnt += customers[j]
            else:
                cnt += customers[j]
            if j - i + 1 > minutes:
                if grumpy[i] == 1:
                    cnt -= customers[i]
                i += 1
            j += 1
            res = max(res, cnt)
        return sumCnt + res


# @lc code=end

