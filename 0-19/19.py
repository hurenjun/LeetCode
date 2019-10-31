# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        x, y, step = None, head, 0
        while y is not None:
            y = y.next
            if step >= n:
                if x is None:
                    x = head
                else:
                    x = x.next
            step += 1
        if x is None:
            head = head.next
        elif x.next is not None:
            x.next = x.next.next
        return head
                
s = Solution()
head, prev = None, None
for x in [1, 2, 3, 4, 5]:
    node = ListNode(x)
    if head is None:
        head = node
    if prev is not None:
        prev.next = node
    prev = node
    
answer = s.removeNthFromEnd(head, 0)
node = answer
while node is not None:
    print(node.val)
    node = node.next
