# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (not p and q) or (p and not q):
                return False
            if not p and not q:
                return True
            left = isSameTree(p.left, q.left)
            right = isSameTree(p.right, q.right)
            return (p.val == q.val) and left and right
        if root == None:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return isSameTree(root, subRoot) or left or right