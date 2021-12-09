#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        res = []
        if not len(l1) and not len(l2):
            return 0
        elif not len(l1) and len(l2):
            return l2
        elif len(l1) and not len(l2):
            return l1
        else:
            if len(l1) == len(l2):
                for i in range(len(l1)):
                    
      
# @lc code=end

