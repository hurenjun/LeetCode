class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []
        if root is None:
            return answer
        layer = [root]
        depth = 0
        while layer:
            answer.append([])
            tmp = []
            for node in layer:
                answer[-1].append(node.val)
                if not node.left is None:
                    tmp.append(node.left)
                if not node.right is None:
                    tmp.append(node.right)
            layer = tmp
            if depth % 2 == 1:
                answer[-1] = answer[-1][::-1]
            depth += 1
        return answer
            
        

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
answer = s.zigzagLevelOrder(root)  
print(answer)

