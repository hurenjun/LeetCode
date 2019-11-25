# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = head
        head, tail = None, None
        while not x is None:
            if not x.next is None and x.next.val == x.val:
                val = x.val
                while not x is None and x.val == val:
                    x = x.next
            else:
                if head is None:
                    head = tail = x
                else:
                    tail.next = x
                    tail = x
                x = x.next
                tail.next = None
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
l = makeList([1,1,1,2,3])
answer = s.deleteDuplicates(l)
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next