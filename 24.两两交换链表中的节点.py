#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 直接进行遍历，新建一个空的头节点，进行连接最开始断开的头节点与第二个节点
        slow, slow.next = ListNode(0), head
        tmp = slow
        while tmp.next and tmp.next.next:
            node1, node2 = tmp.next, tmp.next.next
            tmp.next, node1.next = node2, node2.next
            node2.next = node1
            tmp = tmp.next.next
        return slow.next


        

# @lc code=end

