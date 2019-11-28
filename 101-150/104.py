class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        inorderMapper = dict()
        for idx, x in enumerate(inorder):
            inorderMapper[x] = idx
            
        def dfs(subPre, subIn, inOffset):
            if not subPre:
                return None
            sep = inorderMapper[subPre[0]] - inOffset
            x = TreeNode(subPre[0])
            x.left = dfs(subPre[1:sep+1], subIn[:sep], inOffset)
            x.right = dfs(subPre[sep+1:], subIn[sep+1:], inorderMapper[subPre[0]] + 1)
            return x
            
        root = dfs(preorder, inorder, 0)
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
answer = s.buildTree([1,2,3,4], [1,2,3,4])  
#print(answer)
traversal = []
outInorderTraversal(answer)
print(traversal)
