class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, x):
        if not x.left is None:
            self.inorderTraversal(x.left)
        self.traversal.append(x.val)
        if not x.right is None:
            self.inorderTraversal(x.right)
        return
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.traversal = []
        self.inorderTraversal(root)
        #print(self.traversal)
        i = 0
        while i + 1 < len(self.traversal) and self.traversal[i] < self.traversal[i + 1]:
            i += 1
        if i + 1 == len(self.traversal):
            return True
        else:
            return False

'''
traversal = []
def inorderTraversal(x):
    if not x.left is None:
        inorderTraversal(x.left)
    traversal.append(x.val)
    if not x.right is None:
        inorderTraversal(x.right)
    return
'''
        
s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node1
node2.right = node3
root = node2

answer = s.isValidBST(root)  
print(answer)

'''
for root in answer:
    traversal = []
    inorderTraversal(root)
    print(traversal)
'''