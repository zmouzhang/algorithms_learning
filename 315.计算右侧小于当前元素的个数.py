#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        for i in range(len(nums) - 1):
            j = i + 1
            num = 0
            while j < len(nums):
                if nums[j] < nums[i]:
                    num += 1
                j += 1
            counts[i] = nums
        counts.append(0)
        return counts

# @lc code=end

