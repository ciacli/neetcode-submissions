# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        def findDepth(node):
            if not node:
                return
            findDepth(node.left)
            findDepth(node.right)
            left = d[node.left] if node.left else -1
            right = d[node.right] if node.right else -1
            d[node] = max(left, right) + 1
        ans = [0]
        def walk(node):
            if not node:
                return
            left = d.get(node.left, -1) + 1
            right = d.get(node.right, -1) + 1
            width = left + right
            print(width)
            if width > ans[0]:
                ans[0] = width
            walk(node.left)
            walk(node.right)
        findDepth(root)
        walk(root)
        return ans[0]