#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 解法一：双指针从0开始
        # length = len(nums)
        # p0, p1 = 0, 0
        # for i in range(length):
        #     if nums[i] == 1:
        #         nums[p1], nums[i] = nums[i], nums[p1]
        #         p1 += 1
        #     elif nums[i] == 0:
        #         nums[p0], nums[i] = nums[i], nums[p0]
        #         if p0 < p1:
        #             nums[i], nums[p1] = nums[p1], nums[i]
        #         p0 += 1
        #         p1 += 1
        
        # 解法二： 双指针，头尾各一个
        # 1，如果nums[i]为2 ，将nums[i]与nums[p2]互换，直到将数组中的2全部放到数组最后面；
        # 2，如果nums[i]为0，将nums[i]与nums[p0]互换，然后p0自增1， i自增1
        # 3，直到i小于p2，结束遍历
        length = len(nums)
        i, p0, p2 = 0, 0, length - 1
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1


# @lc code=end

