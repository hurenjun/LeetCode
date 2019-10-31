# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, now = None, None
        while not (l1 is None and l2 is None):
            if l1 is None or not l2 is None and l2.val < l1.val:
                if head is None:
                    head = now = l2
                else:
                    now.next = l2
                    now = now.next
                l2 = l2.next
            else:
                if head is None:
                    head = now = l1
                else:
                    now.next = l1
                    now = now.next
                l1 = l1.next
            now.next = None
        return head
    
def makeList(ls):
    head, prev = None, None
    for x in ls:
        node = ListNode(x)
        if head is None:
            head = node
        if prev is not None:
            prev.next = node
        prev = node
    return head
    
s = Solution()
l1 = makeList([1， 2， 4])
l2 = makeList([1， 3， 4])
answer = s.mergeTwoLists(l1, l2)
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next