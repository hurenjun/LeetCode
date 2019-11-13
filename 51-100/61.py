# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        p, length = head, 0
        while k > 0:
            p = p.next
            length += 1
            k -= 1
            if p is None:
                k = k % length
                length = 0
                p = head
            
        if p == head:
            return head
        
        q = head
        while not p.next is None:
            p, q = p.next, q.next
        p.next = head
        head = q.next
        q.next = None
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
l = makeList(range(1, 3))
answer = s.rotateRight(l, 10)
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next