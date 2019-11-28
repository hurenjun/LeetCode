class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        n, x = 0, head
        while not x is None:
            x = x.next
            n += 1
        
        self.now = head
        def makeTree(start, end):
            if start > end:
                return None
            m = (start + end) // 2
            left = makeTree(start, m - 1)
            node = TreeNode(self.now.val)
            self.now = self.now.next
            right = makeTree(m + 1, end)
            node.left, node.right = left, right
            return node
        
        return makeTree(0, n - 1)
            
                

def outInorderTraversal(x):
    if not x.left is None:
        inorderTraversal(x.left)
    traversal.append(x.val)
    if not x.right is None:
        inorderTraversal(x.right)
    return

        
def makeTree(vals):
    nodes = [TreeNode(x) if not x is None else None for x in vals]
    father, left, right = 0, 1, 2
    while right < len(vals):
        nodes[father].left = nodes[left]
        nodes[father].right = nodes[right]
        father, left, right = father + 1, left + 2, right + 2
    return nodes[0]

root = makeTree([3,9,20,None,None,15,7])

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

head = makeList([-10, -3, 0, 5, 9])


s = Solution()
answer = s.sortedListToBST(head)  
#print(answer)
traversal = []
outInorderTraversal(answer)
print(traversal)
