# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ans = [1]
        def walk(node, level):
            if node == None:
                return 
            if level > ans[0]:
                ans[0] = level
            walk(node.left, level + 1)
            walk(node.right, level + 1)
        walk(root, 1)
        return ans[0]
