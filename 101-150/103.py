class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        
        def traversal(depth, x):
            if x is None:
                return
            if depth > self.depth:
                self.depth = depth
            traversal(depth + 1, x.left)
            traversal(depth + 1, x.right)
            return
        
        if not root is None:
            traversal(1, root)
        return self.depth
            
        

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

#traversal = []
#outInorderTraversal(root)
#print(traversal)

s = Solution()
answer = s.maxDepth(root)  
print(answer)

