class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def makeTree(subNums):
            if not subNums:
                return None
            x = len(subNums) // 2
            node = TreeNode(subNums[x])
            node.left = makeTree(subNums[:x])
            node.right = makeTree(subNums[x+1:])
            return node
        
        return makeTree(nums)

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
answer = s.sortedArrayToBST([-10,-3,0,5,9])  
#print(answer)
traversal = []
outInorderTraversal(answer)
print(traversal)
