# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node):
            if node == None:
                return 
            nonlocal k
            if k < 1:
                return
            dfs(node.left)
            if k == 1:
                nonlocal ans
                ans = node.val
            k -= 1
            dfs(node.right)
        dfs(root)
        return ans
            