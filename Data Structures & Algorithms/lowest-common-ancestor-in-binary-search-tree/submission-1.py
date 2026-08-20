# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, node, path):
            if root.val == node.val:
                return 
            if root.val > node.val:
                path.append(-1)
                dfs(root.left, node, path)
            else:
                path.append(1)
                dfs(root.right, node, path)
        def findLCS(root, path1, path2):
            if not path1 or not path2 or path1[0] != path2[0]:
                return root
            if path1[0] == -1:
                return findLCS(root.left, path1[1:], path2[1:])
            else:
                return findLCS(root.right, path1[1:], path2[1:])
        path1 = []
        path2 = []
        dfs(root, p, path1)
        dfs(root, q, path2)
        return findLCS(root, path1, path2)
            
            