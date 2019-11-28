class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev, self.first, self.second = None, None, None
        self.inorderTraversal(root)
        if not self.first is None and not self.second is None:
            self.first.val, self.second.val = self.second.val, self.first.val
        return None
    
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        if not self.prev is None:
            if root.val < self.prev.val:
                if self.first is None:
                    self.first = self.prev
                    self.second = root
                else:
                    self.second = root
        self.prev = root
        self.inorderTraversal(root.right)
        return None


def inorderTraversal(x):
    if not x.left is None:
        inorderTraversal(x.left)
    traversal.append(x.val)
    if not x.right is None:
        inorderTraversal(x.right)
    return

        
s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node3
node3.right = node2
root = node1

answer = s.recoverTree(root)  
#print(answer)

traversal = []
inorderTraversal(root)
print(traversal)
