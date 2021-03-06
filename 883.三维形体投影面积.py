#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(grid[i][j]>0  for i in range(len(grid)) for j in range(len(grid[0])))
        xz = sum(max(i)  for i in grid)
        yz = sum(max(i)  for i in zip(*grid))
        return xy+xz+yz
# @lc code=end

