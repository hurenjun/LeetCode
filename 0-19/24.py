# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        now, now_and_next = head, None if head is None else head.next
        prev = None
        while not now_and_next is None:
            if prev is None:
                head = now_and_next
            else:
                prev.next = now_and_next
            tmp = now_and_next.next
            now_and_next.next = now
            now.next = tmp
            prev = now
            now, now_and_next = tmp, None if tmp is None else tmp.next
        return head