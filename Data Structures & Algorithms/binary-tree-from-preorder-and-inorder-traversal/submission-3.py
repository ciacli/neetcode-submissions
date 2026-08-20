# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        indexes = {}
        for i in range(n):
            indexes[inorder[i]] = i
        idx = 0
        def dfs(lo, hi):
            nonlocal idx
            if lo > hi:
                return None
            node = TreeNode(preorder[idx])
            idx += 1
            left = dfs(lo, indexes[node.val] - 1)
            right = dfs(indexes[node.val] + 1, hi)
            node.left = left
            node.right = right
            return node
        
        return dfs(0, n - 1)


