# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head_less, tail_less, head_ge, tail_ge = None, None, None, None
        while not head is None:
            if head.val < x:
                if head_less is None:
                    head_less = tail_less = head
                    head = head.next
                    tail_less.next = None
                else:
                    tail_less.next = head
                    tail_less = head
                    head = head.next
                    tail_less.next = None
            else:
                if head_ge is None:
                    head_ge = tail_ge = head
                    head = head.next
                    tail_ge.next = None
                else:
                    tail_ge.next = head
                    tail_ge = head
                    head = head.next
                    tail_ge.next = None
            
        if head_less is None:
            return head_ge
        else:
            tail_less.next = head_ge
            return head_less
        
    
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
l = makeList([1,4,3,2,5,2])
answer = s.partition(l, 0)
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next