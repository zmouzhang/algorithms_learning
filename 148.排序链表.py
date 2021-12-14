#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 暴力拆解实现，时间复杂度为O(n), 空间复杂度为O(n)
        # tmp = []
        # while head:
        #     tmp.append(head.val)
        #     head = head.next
        # # print(sorted(tmp))
        # move = dummy = ListNode(0)
        # for item in sorted(tmp):
        #     dummy.next = ListNode(item)
        #     dummy = dummy.next
        # return move.next
        # 可以利用归并排序的方法进行实现
        if not head or not head.next:
            return head
        #查找到链表的中间节点，利用快慢指针
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        # 归并递归分割
        left = self.sortList(head)
        right = self.sortList(mid)
        # 合并左右链表
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

# @lc code=end

