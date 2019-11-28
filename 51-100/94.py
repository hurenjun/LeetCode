class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        if root is None:
            return answer
        stack = [root]
        while stack:
            x = stack.pop()
            if x.left == None and x.right == None:
                answer.append(x.val)
            else:
                if not x.right is None:
                    stack.append(x.right)
                    x.right = None
                stack.append(x)
                if not x.left is None:
                    stack.append(x.left)
                    x.left = None
        return answer
        
s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node3
node1.right = node2
root = node1
answer = s.inorderTraversal(root)  
print(answer)