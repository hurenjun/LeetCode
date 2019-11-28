class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorderMapper = dict()
        for idx, x in enumerate(inorder):
            inorderMapper[x] = idx
            
        def dfs(subPost, subIn, inOffset):
            if not subIn:
                return None
            sep = inorderMapper[subPost[-1]] - inOffset
            x = TreeNode(subPost[-1])
            x.left = dfs(subPost[0:sep], subIn[:sep], inOffset)
            x.right = dfs(subPost[sep:-1], subIn[sep+1:], inorderMapper[subPost[-1]] + 1)
            return x
            
        root = dfs(postorder, inorder, 0)
        return root

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



s = Solution()
answer = s.buildTree([9,3,15,20,7], [9,15,7,20,3])  
#print(answer)
traversal = []
outInorderTraversal(answer)
print(traversal)
