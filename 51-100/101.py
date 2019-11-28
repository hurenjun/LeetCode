class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.answer = True
        def dfs(rp, rq):
            if not self.answer:
                return
            if rp is None and rq is None:
                return
            if rp is None or rq is None:
                self.answer = False
                return
            if rp.val != rq.val:
                self.answer = False
                return
            dfs(rp.left, rq.right)
            dfs(rp.right, rq.left)
            return
        
        if root is None:
            return True
        dfs(root.left, root.right)
        return self.answer
        

def outInorderTraversal(x):
    if not x.left is None:
        inorderTraversal(x.left)
    traversal.append(x.val)
    if not x.right is None:
        inorderTraversal(x.right)
    return

        
def makeTree(vals):
    nodes = [TreeNode(x) if not x is None else None for x in vals]
    root = nodes[0]
    father, left, right = 0, 1, 2
    while right < len(vals):
        nodes[father].left = nodes[left]
        nodes[father].right = nodes[right]
        father, left, right = father + 1, left + 2, right + 2
    return root

root = makeTree([1,2,2,None,3,None,3])

#traversal = []
#outInorderTraversal(root)
#print(traversal)

s = Solution()
answer = s.isSymmetric(root)  
print(answer)

