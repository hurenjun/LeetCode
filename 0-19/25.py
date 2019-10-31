# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head
        
        init = ListNode(0)
        init.next = head
        now = init
        while not now.next is None:
            stop = now
            for _ in range(k):
                stop = stop.next
                if stop is None:
                    break
            if stop is None:
                break
            x, y = now.next, None
            now.next = stop
            for idx in range(k):
                if idx == 0:
                    tmp = x.next
                    x.next = stop.next
                    tail = x
                    x, y = tmp, x
                else:
                    tmp = x.next
                    x.next = y
                    x, y = tmp, x
            now = tail
            
        return init.next
        
    
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
l = makeList(range(1, 11))
answer = s.reverseKGroup(l, 4)
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next