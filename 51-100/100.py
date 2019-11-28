class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.answer = True
        
        def traversal(rp, rq):
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
            traversal(rp.left, rq.left)
            traversal(rp.right, rq.right)
            return
        
        traversal(p, q)
        return self.answer
            


def outInorderTraversal(x):
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

answer = s.isSameTree(root, root)  
print(answer)

#traversal = []
#outInorderTraversal(root)
#print(traversal)
