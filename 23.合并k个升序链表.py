#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 顺序合并， 时间优化率为16%以上
        def merge(l1, l2):
            res = tmp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    tmp.next, l1 = l1, l1.next
                else:
                    tmp.next, l2 = l2, l2.next
                tmp = tmp.next
            tmp.next = l1 if l1 else l2
            return res.next
        ans = None
        for item in lists:
            ans = merge(ans, item)
        return ans


        # 利用归并排序 时间优化率为 60%以上
        def merg(l1, l2):
            res = tmp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    tmp.next, l1 = l1, l1.next
                else:
                    tmp.next, l2 = l2, l2.next
                tmp = tmp.next
            tmp.next = l1 if l1 else l2
            return res.next
        def merg_sort(lists, l, r):
            if l == r:
                return lists[l]
            middle = (l+r)//2
            L = merg_sort(lists, l, middle)
            R = merg_sort(lists, middle+1, r)
            return merg(L,R)
        if not lists:
            return None
        n = len(lists)
        return merg_sort(lists, 0, n-1)

        # 利用最小堆
        import heapq
        min_heap = []
        # 将链表依次入堆
        for item in lists:
            while item:
                heapq.heappush(min_heap, item.val)
                item = item.next
        res = tmp = ListNode(0)
        # 依次出堆 时间优化率为99%以上
        while min_heap:
            tmp.next = ListNode(heapq.heappop(min_heap))
            tmp = tmp.next
        return res.next
        
# @lc code=end

