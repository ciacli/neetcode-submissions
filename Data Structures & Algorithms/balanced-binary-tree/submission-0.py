# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = [True]
        def dfs(node):
            if node == None:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                ans[0] = False
            return max(left, right) + 1
        dfs(root)
        return ans[0]
            
