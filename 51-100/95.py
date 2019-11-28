class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def copyTree(self, root, offset):
        if root is None:
            return None
        copy = TreeNode(root.val + offset)
        left_copy = right_copy = None
        if not root.left is None:
            left_copy = self.copyTree(root.left, offset)
        if not root.right is None:
            right_copy = self.copyTree(root.right, offset)
        copy.left, copy.right = left_copy, right_copy
        return copy
        
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        from collections import defaultdict
        trees = defaultdict(list)
        trees[0].append(None)
        trees[1].append(TreeNode(1))
        for k in range(2, n + 1):
            for root_num in range(1, k + 1):
                for left_tree in trees[root_num - 1]:
                    left_tree_copy = self.copyTree(left_tree, 0)
                    for right_tree in trees[k - root_num]:
                        right_tree_copy = self.copyTree(right_tree, root_num)
                        root = TreeNode(root_num)
                        root.left, root.right = left_tree_copy, right_tree_copy
                        trees[k].append(root)
        return trees[n]
    

traversal = []
def inorderTraversal(x):
    if not x.left is None:
        inorderTraversal(x.left)
    traversal.append(x.val)
    if not x.right is None:
        inorderTraversal(x.right)
    return

        
s = Solution()
'''
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node3
node1.right = node2
root = node1
'''

answer = s.generateTrees(4)  
#print(answer)
for root in answer:
    traversal = []
    inorderTraversal(root)
    print(traversal)