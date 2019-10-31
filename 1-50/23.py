# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        prev = head = ListNode(0)
        h = []
        for idx, node in enumerate(lists):
            if not node is None:
                heapq.heappush(h, (node.val, idx))
        
        while len(h) > 0:
            val, idx = heapq.heappop(h)
            node = ListNode(val)
            prev.next = node
            prev = node
            lists[idx] = lists[idx].next
            if not lists[idx] is None:
                heapq.heappush(h, (lists[idx].val, idx))
        return head.next
        
    
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
l1 = makeList([1, 4, 5])
l2 = makeList([1, 3, 4])
l3 = makeList([2, 6])
answer = s.mergeKLists([l1, l2, l3])
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next