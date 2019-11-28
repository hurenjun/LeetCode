# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        node_m_m1, node_m, node_n_p1 = None, None, None  # nodes at m-1, m, and n+1, respectively
        x = head
        walked = 1
        rev_tail = None
        while x != None:
            y = x.next
            if walked == m -1:
                node_m_m1 = x
            elif walked == n + 1:
                node_n_p1 = x
                break
            elif walked == m:
                node_m = x
                rev_tail = x
                x.next = None
            elif m + 1 <= walked <= n:
                x.next = rev_tail
                rev_tail = x
            x = y
            walked += 1
        if m == 1:
            head = rev_tail
        else:
            node_m_m1.next = rev_tail
        node_m.next = node_n_p1
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
l = makeList([1,2,3,4,5])
answer = s.reverseBetween(l, 1, 5)
#print(answer)
node = answer
while node is not None:
    print(node.val)
    node = node.next