#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        TODO: 按照k个一组的链表翻转整个链表，剩余不足K的数据不翻转
        """
        if head is None or k < 2: return head
        dummy = ListNode(0)
        dummy.next = head
        start, end = dummy, head
        count = 0
        while end:
            count += 1
            if count % k == 0:
                start = self.reserver(start, end.next)
                end = start.next
            else:
                end = end.next
        return dummy.next
    def reserver(self, start, end):
        """
        TODO: 翻转链表中从start、end之间的节点
        @param: start 开始节点 end 结束节点
        """
        prev, curr = start, start.next
        first = curr
        while curr != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # 将空的头节点重新指向反转后的第一个节点。
        start.next = prev
        # 将最开始的节点指向剩余的节点
        first.next = curr
        return first
# @lc code=end
